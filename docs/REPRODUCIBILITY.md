# Reproducibility Guide

## Reproduction Levels

This package supports four levels of replication:

1. **Inventory validation.** Check the expected subjects, MRs, source test
   data, mutant sources, and final result workbooks.
2. **Portable execution check.** Run an actual MR on the original TSQ program
   and a selected mutant using a packaged source test case.
3. **Result inspection and reanalysis.** Inspect the final per-subject,
   per-mutant, per-formula, variant, and statistical-test workbooks.
4. **Complete experiment re-execution.** Regenerate test executions, coverage
   traces, spectrum data, and final rankings using the original subject
   drivers after adapting them to the local environment.

The first three levels are available directly from the repository. The fourth
requires the configuration and generated intermediates described below.

## Environment

The experiment harness is written in Python. The larger subjects are written
in C and are executed through Python harnesses.

Install the Python dependencies with:

```bash
python3 -m pip install -r requirements.txt
```

The C subjects additionally require a C compiler and compatible statement
coverage tools. Subject-specific source and build utilities are retained under
`code/Tcas/`, `code/PT/`, `code/PT2/`, and `code/Grep/`.

## Directly Runnable Checks

From the repository root, validate the packaged inventory:

```bash
python3 scripts/validate_artifacts.py
```

The checker reports the documented absence of Grep mutants 51-56 as a known
packaging gap. Unexpected missing artifacts still cause validation to fail.

Run the portable TSQ example:

```bash
python3 scripts/demo_tsq.py
```

The script loads a packaged TSQ source test case, applies one of the nine MRs,
and compares the MR result for the original program with that for `Mutant1`.
It searches deterministically for the first packaged MG that satisfies the MR
on the original program and violates it on the mutant, then prints the source
test case, follow-up test case, MR identifier, and both outcomes.

This check demonstrates the use of a real subject, MR, test case, and mutant
from the experiment. It does not replace the full fault-localization pipeline,
which requires many MGs and their statement-coverage data.

## Complete Subject-Level Workflow

For each subject, the original study performed the following steps:

1. Select the original program or a mutant implementation.
2. Load a source test case from `data/<subject>/`.
3. Generate follow-up test cases using the subject MR implementation.
4. Execute the test cases and classify each MG as MR-satisfying or
   MR-violating.
5. Collect statement coverage for every individual test case.
6. Construct the spectrum information for the selected MFL technique.
7. Apply the 30 risk formulas and rank the program elements.
8. Calculate EXAM and TOP-N and write the analysis workbooks.

The Python subjects combine several of these stages in `<subject>_test.py`.
PT, PT2, and Grep additionally provide execution and statement-coverage
scripts. The shared spectrum, formula, and metric implementations are in
`publicFun.py`.

## Why the Original Drivers Need Configuration

The original drivers preserve the research workflow and historical internal
labels, but they are not portable command-line applications. Some scripts
refer to absolute paths in the original experiment environment and expect
generated files that are not committed to this package, including:

- follow-up test inputs and program outputs;
- per-test statement-coverage traces;
- serialized MG and execution-profile data;
- intermediate matrices and ranking data; and
- output workbook locations.

Before a complete rerun, replace these paths with local directories and execute
the subject stages in their original order. The repository does not include
the complete generated workspace because it is approximately 25 GB. These
files are generated intermediates rather than manually curated experimental
inputs.

## Mutant and Test-Case Filtering

A faulty version enters the fault-localization analysis only when at least one
executed MG violates its MR. If every MG satisfies its MR, the available MT
executions have not exposed failure evidence for MFL.

FAILTIM also requires MR-violating MGs to identify likely failure-revealing
test cases. A source test case whose associated MGs are all MR-satisfying is
therefore excluded. The same filtered test cases are used for all four
techniques so that they are compared under identical inputs.

Both checks depend only on observable MR satisfaction/violation results. They
do not require the pass/fail oracle of an individual test case.

## Final Results and Statistical Analysis

The packaged workbooks are documented in
[`../results/README.md`](../results/README.md).

For the technique comparisons, the unit of analysis in the Wilcoxon
Signed-Rank test is a mutant. For each mutant, technique, and evaluation metric,
the results obtained using all 30 risk formulas are averaged. When two
techniques are compared, the two values for the same mutant form one paired
observation. Tests are conducted separately for each evaluation metric.

## Current Packaging Status

The source directories for selected Grep mutants 51-56 were not present in the
recovered experiment workspace. Their mutant identifiers, preserved output
records, and faulty source-line locations establish that they were used in the
study, but the exact source replacements cannot be reconstructed reliably from
those records alone. They are therefore documented as a known source-package
gap rather than replaced with inferred mutations.

See [`MUTANTS.md`](MUTANTS.md#packaging-status) for the verified mapping and
the exact inventory status.
