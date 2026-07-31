#!/usr/bin/env python3
"""Run a portable metamorphic-testing example using the packaged TSQ artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TSQ_DIR = ROOT / "code/TSQ"
DATA_PATH = ROOT / "data/TSQ/source-test-cases.json"

sys.path.insert(0, str(TSQ_DIR))

from TSQ import MTG  # noqa: E402
from mutants.Mutant1 import Mutant1  # noqa: E402
from mutants.Original import Trisquare  # noqa: E402


OUTCOME_LABELS = {
    0: "MR-satisfying",
    1: "MR-violating",
    2: "invalid source test case",
}


def load_source_cases() -> list[list[float]]:
    payload = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    if isinstance(payload, str):
        payload = json.loads(payload)
    return payload["random_input"]


def find_example() -> tuple[list[float], int, list[float], int, int]:
    original = Trisquare()
    mutant = Mutant1()
    for source in load_source_cases():
        original_results, original_followups = MTG(source, original)
        mutant_results, mutant_followups = MTG(source, mutant)
        for index, (original_result, mutant_result) in enumerate(
            zip(original_results, mutant_results),
            start=1,
        ):
            if original_result == 0 and mutant_result == 1:
                followup = mutant_followups[index - 1]
                if followup != original_followups[index - 1]:
                    raise RuntimeError("Original and mutant MR transformations differ.")
                return source, index, followup, original_result, mutant_result
    raise RuntimeError("No packaged TSQ example exposes Mutant1 through an MR.")


def main() -> None:
    source, mr_number, followup, original_result, mutant_result = find_example()
    print("Portable TSQ metamorphic-testing example")
    print("----------------------------------------")
    print("Subject:        TSQ")
    print("Mutant:         Mutant1")
    print(f"MR:             MR{mr_number}")
    print(f"Source test:    {source}")
    print(f"Follow-up test: {followup}")
    print(
        "Original:       "
        f"{OUTCOME_LABELS[original_result]} (outcome={original_result})"
    )
    print(
        "Mutant1:        "
        f"{OUTCOME_LABELS[mutant_result]} (outcome={mutant_result})"
    )
    print("\nThe MG exposes Mutant1 without using an individual-test pass/fail oracle.")


if __name__ == "__main__":
    main()
