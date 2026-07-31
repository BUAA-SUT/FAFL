# Reproducibility Guide

## What Can Be Reproduced from This Package

The package exposes three levels of replication:

1. **Artifact inspection.** The selected subject programs, MRs, source test
   cases, and available mutant source versions can be inspected directly.
2. **Experiment re-execution.** The subject drivers and coverage scripts can be
   rerun after configuring compiler/tool paths and output directories for the
   local machine.
3. **Result inspection and reanalysis.** The aggregate workbooks under
   `results/` contain the reported subject-level technique results and
   statistical-test data.

The repository does not include the complete generated workspace of
per-execution coverage traces and intermediate matrices, which is approximately
25 GB. Those files are outputs of the execution and coverage-collection stages.

## Environment

The experiment harness is written in Python and the larger subjects are written
in C.

Python dependencies are listed in `requirements.txt`:

```bash
python -m pip install -r requirements.txt
```

The C subjects require a C compiler and the coverage tooling used by the
subject-specific scripts. The Grep, PT, and PT2 directories contain their
subject-specific sources and build files where available.

## Subject-Level Workflow

For each subject:

1. Select an original or mutant implementation.
2. Load a source test case from `data/<subject>/`.
3. Generate follow-up test cases using the MR implementation under
   `code/<subject>/`.
4. Execute all test cases and evaluate each MG as MR-satisfying or
   MR-violating.
5. Collect statement coverage for the individual test cases.
6. Construct the spectrum information required by the selected MFL technique.
7. Apply the risk formulas and record the resulting program-element rankings.

The Python subjects combine most steps in `<subject>_test.py`. PT, PT2, and
Grep additionally provide statement-coverage scripts. Run the Python drivers
from the repository root with the root directory on `PYTHONPATH`, for example:

```bash
PYTHONPATH=. python code/TSQ/TSQ_test.py
```

## Path Configuration

The original research scripts were developed against a local experiment
workspace and some retain absolute paths. Before running them on another
machine, replace those paths with local locations for:

- subject-program binaries;
- generated follow-up inputs and outputs;
- statement-coverage files;
- intermediate JSON or matrix files; and
- final result workbooks.

The source package preserves these scripts for traceability. A portable
one-command runner is not claimed by the current artifact.

## Mutant and Test-Case Filtering

A faulty version is included in the fault-localization evaluation only if at
least one executed MG violates its MR. If no MR is violated, MT has not exposed
failure evidence from which MFL can perform localization.

FAILTIM also requires MR-violating MGs to infer failure-revealing information.
A source test case whose associated MGs are all MR-satisfying is therefore
excluded. The same filtered test cases are used for all four techniques to
ensure a controlled comparison.

These checks use only observable compilation status and MR
satisfaction/violation results. They do not require the pass/fail oracle of an
individual test case.

## Statistical Analysis

The final statistical data are in
`results/statistical-tests.xlsx`. For each mutant, technique, and evaluation
metric, the results obtained using the 30 risk formulas are averaged. When two
techniques are compared, the two averages for the same mutant form one paired
observation. The Wilcoxon Signed-Rank test is then applied across mutants,
separately for each evaluation metric.

## Current Packaging Check

The local source workspace supplied for this repository does not contain the
source directories for selected Grep mutants 51-56, although the experiment
outputs and final results refer to them. Their faulty source lines have been
recovered from the preserved experiment driver and verified against the
nonzero entries in the original result vectors, but the exact source-code
replacements have not been recovered. See
[`MUTANTS.md`](MUTANTS.md#packaging-status) for the verified mapping. The six
source directories or equivalent mutation records must still be restored to
make the selected-mutant source inventory complete.
