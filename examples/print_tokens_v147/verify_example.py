#!/usr/bin/env python3
"""Verify the observable PT v147 example in an isolated temporary directory."""

from __future__ import annotations

import csv
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXAMPLE = Path(__file__).resolve().parent
PT = ROOT / "code" / "PT"


def build(source: Path, output: Path) -> None:
    compiler = shutil.which("cc") or shutil.which("gcc") or shutil.which("clang")
    if compiler is None:
        raise SystemExit("A C compiler (cc, gcc, or clang) is required.")
    subprocess.run(
        [compiler, "-std=gnu89", "-w", str(source), "-o", str(output)],
        check=True,
        cwd=source.parent,
    )


def run(binary: Path, input_path: Path) -> str:
    completed = subprocess.run(
        [str(binary)],
        input=input_path.read_bytes(),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True,
    )
    return completed.stdout.decode("utf-8", errors="replace")


def category_count(output: str) -> int:
    return sum(
        1
        for line in output.splitlines()
        if "," in line and ("identifier" in line or "keyword" in line)
    )


def packaged_inputs() -> dict[str, str]:
    with (ROOT / "data" / "PT" / "RandomInput.csv").open(newline="") as handle:
        return {row["name"]: row["value"] for row in csv.DictReader(handle)}


def case_data() -> dict[str, dict[str, str]]:
    with (EXAMPLE / "case-data.csv").open(newline="") as handle:
        return {row["role"]: row for row in csv.DictReader(handle)}


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="mfl-v147-") as directory:
        work = Path(directory)
        for name in ("print_tokens.c", "tokens.h", "stream.h"):
            shutil.copy2(PT / name, work / name)

        original_source = work / "print_tokens.c"
        mutant_source = work / "print_tokens_v147.c"
        mutant_text = original_source.read_text()
        original = "token_ptr->token_id=keyword(next_st);"
        mutated = "token_ptr->token_id=keyword(-next_st);"
        if mutant_text.count(original) != 1:
            raise RuntimeError("Expected exactly one v147 mutation site.")
        mutant_source.write_text(mutant_text.replace(original, mutated))

        original_binary = work / "print_tokens_original"
        mutant_binary = work / "print_tokens_v147"
        build(original_source, original_binary)
        build(mutant_source, mutant_binary)

        source_input = EXAMPLE / "source.txt"
        follow_input = EXAMPLE / "follow-up.txt"
        inputs = packaged_inputs()
        data = case_data()
        assert source_input.read_text() == inputs[data["source"]["input_name"]]
        assert follow_input.read_text() == inputs[data["follow-up"]["input_name"]]

        original_source_output = run(original_binary, source_input)
        original_follow_output = run(original_binary, follow_input)
        mutant_source_output = run(mutant_binary, source_input)
        mutant_follow_output = run(mutant_binary, follow_input)

        assert category_count(original_source_output) == 2
        assert category_count(original_follow_output) == 2
        assert category_count(mutant_source_output) != 2
        assert category_count(mutant_follow_output) == 2
        assert data["source"]["line_231_covered"] == "1"
        assert data["follow-up"]["line_231_covered"] == "0"

        print("Original source output:\n" + original_source_output)
        print("Original follow-up output:\n" + original_follow_output)
        print("Mutant source output:\n" + mutant_source_output)
        print("Mutant follow-up output:\n" + mutant_follow_output)
        print("MR1: original satisfies; printtokens_v147 violates")
        print("Coverage: Line 231 is covered by t_s and not covered by t_f")


if __name__ == "__main__":
    main()
