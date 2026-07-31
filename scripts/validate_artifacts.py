#!/usr/bin/env python3
"""Validate the artifact inventory reported in the paper and repository docs."""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXPECTED_MRS = {
    "TSQ": 9,
    "DM": 10,
    "SMM": 15,
    "KNN": 11,
    "Tcas": 9,
    "PT": 11,
    "PT2": 11,
    "Grep": 12,
}

EXPECTED_MUTANTS = {
    "TSQ": {1, 2, 3, 4, 5},
    "DM": {1, 2, 3, 4, 5},
    "SMM": {2, 3, 4, 5, 6, 7},
    "KNN": {1, 2, 4},
    "Tcas": set(range(1, 21)),
    "PT": {
        2,
        32,
        58,
        88,
        120,
        134,
        161,
        201,
        202,
        205,
        210,
        215,
        220,
        240,
        260,
        354,
        355,
        360,
        364,
        366,
        368,
    },
    "PT2": set(range(1, 22)),
    "Grep": {
        5,
        10,
        11,
        12,
        13,
        14,
        16,
        18,
        20,
        23,
        25,
        26,
        27,
        29,
        30,
        31,
        34,
        35,
        36,
        38,
        39,
        40,
        41,
        43,
        46,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
    },
}

KNOWN_MISSING_MUTANTS = {
    "Grep": {51, 52, 53, 54, 55, 56},
}

MR_FILES = {
    "TSQ": ROOT / "code/TSQ/TSQ.py",
    "DM": ROOT / "code/DM/DM.py",
    "SMM": ROOT / "code/SMM/SMM.py",
    "KNN": ROOT / "code/KNN/KNN.py",
    "Tcas": ROOT / "code/Tcas/Tcas.py",
    "PT": ROOT / "code/PT/PT.py",
    "PT2": ROOT / "code/PT2/PT2.py",
    "Grep": ROOT / "code/Grep/MRs/MR.py",
}

REQUIRED_DATA = {
    "TSQ": ROOT / "data/TSQ/source-test-cases.json",
    "DM": ROOT / "data/DM/source-test-cases.json",
    "SMM": ROOT / "data/SMM/source-test-cases.json",
    "KNN": ROOT / "data/KNN/source-test-cases.json",
    "Tcas": ROOT / "data/Tcas/source-test-cases.json",
    "PT": ROOT / "data/PT/RandomInput.csv",
    "PT2": ROOT / "data/PT2/RandomInput.csv",
    "Grep": ROOT / "data/Grep/RandomInput.csv",
}


def mr_numbers(path: Path) -> set[int]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    numbers = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            match = re.fullmatch(r"MR(\d+)", node.name)
            if match:
                numbers.add(int(match.group(1)))
    return numbers


def mutant_numbers(subject: str) -> set[int]:
    mutant_dir = ROOT / f"code/{subject}/mutants"
    if subject in {"TSQ", "DM", "SMM", "KNN"}:
        return {
            int(match.group(1))
            for path in mutant_dir.glob("Mutant*.py")
            if (match := re.fullmatch(r"Mutant(\d+)\.py", path.name))
        }
    if subject == "Tcas":
        source_path = mutant_dir / "Mutants.py"
        tree = ast.parse(source_path.read_text(encoding="utf-8"))
        return {
            int(match.group(1))
            for node in tree.body
            if isinstance(node, ast.ClassDef)
            if (match := re.fullmatch(r"Mutant(\d+)", node.name))
        }
    prefixes = {"PT": "printtokens_v", "PT2": "printtokens2_v", "Grep": "grep_v"}
    prefix = prefixes[subject]
    return {
        int(path.name.removeprefix(prefix))
        for path in mutant_dir.glob(f"{prefix}*")
        if path.is_dir() and path.name.removeprefix(prefix).isdigit()
    }


def main() -> int:
    failures = []
    known_gaps = []
    print("Artifact inventory")
    print("------------------")
    for subject in EXPECTED_MRS:
        actual_mrs = mr_numbers(MR_FILES[subject])
        expected_mrs = set(range(1, EXPECTED_MRS[subject] + 1))
        actual_mutants = mutant_numbers(subject)
        missing_mrs = expected_mrs - actual_mrs
        missing_mutants = EXPECTED_MUTANTS[subject] - actual_mutants
        documented_missing = missing_mutants & KNOWN_MISSING_MUTANTS.get(subject, set())
        unexpected_missing = missing_mutants - documented_missing
        extra_mutants = actual_mutants - EXPECTED_MUTANTS[subject]
        data_exists = REQUIRED_DATA[subject].is_file()

        status = "OK"
        details = []
        if missing_mrs:
            status = "INCOMPLETE"
            details.append(f"missing MRs {sorted(missing_mrs)}")
        if unexpected_missing:
            status = "INCOMPLETE"
            details.append(f"missing mutants {sorted(unexpected_missing)}")
        if documented_missing:
            if status == "OK":
                status = "KNOWN GAP"
            details.append(f"documented missing mutants {sorted(documented_missing)}")
            known_gaps.append(
                f"{subject}: source directories are unavailable for "
                f"{sorted(documented_missing)}"
            )
        if extra_mutants:
            status = "INCOMPLETE"
            details.append(f"unexpected mutants {sorted(extra_mutants)}")
        if not data_exists:
            status = "INCOMPLETE"
            details.append(f"missing data {REQUIRED_DATA[subject].relative_to(ROOT)}")

        failure_details = [
            detail
            for detail in details
            if not detail.startswith("documented missing mutants")
        ]
        if failure_details:
            failures.extend(f"{subject}: {detail}" for detail in failure_details)
        suffix = f" ({'; '.join(details)})" if details else ""
        print(
            f"{subject:5} {status:10} "
            f"MRs={len(actual_mrs):2}/{EXPECTED_MRS[subject]:2} "
            f"mutants={len(actual_mutants):2}/{len(EXPECTED_MUTANTS[subject]):2} "
            f"data={'yes' if data_exists else 'no'}{suffix}"
        )

    required_results = [
        ROOT / "results/all-techniques.xlsx",
        ROOT / "results/statistical-tests.xlsx",
    ]
    for path in required_results:
        if not path.is_file():
            failures.append(f"missing result workbook: {path.relative_to(ROOT)}")

    if failures:
        print("\nValidation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    if known_gaps:
        print("\nDocumented packaging gaps:")
        for gap in known_gaps:
            print(f"- {gap}")

    print("\nInventory matches the documented packaging status.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
