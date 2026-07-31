# MFL: Improving Metamorphic Fault Localization

This repository is the replication package for the paper **"Improving
Metamorphic Fault Localization: A Framework and a Series of Techniques."**
It contains the subject-program implementations, metamorphic relations (MRs),
source test cases, selected mutants, analysis code, and aggregate experimental
results used in the study.

## Experimental Scope

| Subject | Language | LOC | Mutants | MRs |
| --- | --- | ---: | ---: | ---: |
| TSQ | Python | 43 | 5 | 9 |
| DM | Python | 54 | 5 | 10 |
| SMM | Python | 103 | 6 | 15 |
| KNN | Python | 72 | 3 | 11 |
| Tcas | C / Python harness | 135 | 20 | 9 |
| PT | C / Python harness | 342 | 21 | 11 |
| PT2 | C / Python harness | 355 | 21 | 11 |
| Grep | C / Python harness | 7,309 | 33 | 12 |
| **Total** |  |  | **114** | **88** |

The experiments evaluate 30 risk formulas. The final workbooks are available
under [`results/`](results/).

## Repository Structure

```text
.
|-- code/       Subject programs, MRs, experiment drivers, and selected mutants
|-- data/       Source test cases and supporting test inputs
|-- docs/       Detailed artifact and reproduction documentation
|-- results/    Aggregate results and statistical-test workbooks
`-- publicFun.py
```

Start with:

- [`docs/SUBJECTS.md`](docs/SUBJECTS.md) for the subject-by-subject artifact map;
- [`docs/METAMORPHIC_RELATIONS.md`](docs/METAMORPHIC_RELATIONS.md) for MR
  specifications and their source locations;
- [`docs/MUTANTS.md`](docs/MUTANTS.md) for the selected faulty versions; and
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for environment,
  filtering, and execution details.

The artifact inventory can be checked with:

```bash
python scripts/validate_artifacts.py
```

## Data Included

The package includes the source test cases used for the eight subjects, the MR
implementations that generate follow-up test cases and evaluate MR outcomes,
and the selected mutant source code available in the original experiment
workspace. The aggregate experimental results are also included.

The source directories for six later-added Grep versions (`grep_v51` through
`grep_v56`) were not present in the recovered workspace. Their verified fault
locations and the exact remaining gap are documented in
[`docs/MUTANTS.md`](docs/MUTANTS.md#packaging-status).

Per-execution coverage traces and intermediate matrices are not stored in this
repository because the complete generated workspace is approximately 25 GB.
The coverage-collection scripts are included so that these artifacts can be
regenerated. See [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) for the
distinction between packaged inputs, generated intermediates, and final
results.

## Important Reproduction Note

The experiment drivers preserve the workflow used in the study. Some of the
original scripts refer to machine-specific working directories and external
tools. Configure those paths for the local environment before re-executing the
complete pipeline. The required files and known packaging status are documented
explicitly rather than hidden behind a one-command claim.

## Results

- [`results/all-techniques.xlsx`](results/all-techniques.xlsx) contains the
  aggregate results for the four MFL techniques and their variants.
- [`results/statistical-tests.xlsx`](results/statistical-tests.xlsx) contains
  the Wilcoxon Signed-Rank test data and associated metric sheets.

The unit of analysis in the Wilcoxon Signed-Rank tests is a mutant. For each
mutant, technique, and evaluation metric, results are first averaged over the
30 risk formulas; the values of two techniques for the same mutant then form
one paired observation.
