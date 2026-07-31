# MFL: Improving Metamorphic Fault Localization

This repository is the replication package for the paper **"Improving
Metamorphic Fault Localization: A Framework and a Series of Techniques."**
It provides the subject programs, metamorphic relations (MRs), source test
cases, selected mutants, implementation code, and final experimental results
used to evaluate the proposed MFL framework.

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

The study evaluates four representative MFL techniques, variants of the
MG-based FRI technique, 30 risk formulas, and the EXAM and TOP-N metrics.

## Quick Start

Clone the repository and check the packaged artifact inventory:

```bash
git clone https://github.com/BUAA-SUT/MFL.git
cd MFL
python3 scripts/validate_artifacts.py
```

Run a small, self-contained metamorphic-testing example using an actual TSQ
mutant, an MR implementation, and a source test case from the package:

```bash
python3 scripts/demo_tsq.py
```

The demo shows how the same MG satisfies its MR on the original program but
violates it on a mutant. It is a portable check of the packaged program, MR,
test data, and mutant; it does not rerun the full fault-localization experiment.

To inspect or rerun the original experiment drivers, first install the Python
dependencies:

```bash
python3 -m pip install -r requirements.txt
```

The complete pipeline additionally requires a C compiler for the C subjects,
coverage tools, local path configuration, and regeneration of the intermediate
execution data described in
[`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md).

## Repository Structure

```text
.
|-- code/       Subject programs, MRs, experiment drivers, and selected mutants
|-- data/       Source test cases and supporting test inputs
|-- docs/       Subject, MR, mutant, and reproduction documentation
|-- results/    Final result and statistical-test workbooks
|-- scripts/    Portable artifact checks and demonstrations
`-- publicFun.py
```

Useful entry points:

- [`docs/SUBJECTS.md`](docs/SUBJECTS.md): subject-by-subject artifact map;
- [`docs/METAMORPHIC_RELATIONS.md`](docs/METAMORPHIC_RELATIONS.md): MR
  specifications and implementation locations;
- [`docs/MUTANTS.md`](docs/MUTANTS.md): selected faulty versions and their
  packaging status;
- [`data/README.md`](data/README.md): source-test pools, selected cases, and
  randomization information;
- [`code/README.md`](code/README.md): implementation map for the techniques,
  formulas, metrics, and subject drivers;
- [`results/README.md`](results/README.md): workbook and worksheet guide; and
- [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md): environment,
  filtering, pipeline, and reproduction boundaries.

## Reproduction Paths

The package supports several complementary forms of replication:

| Goal | Starting point | Status |
| --- | --- | --- |
| Check the artifact inventory | `python3 scripts/validate_artifacts.py` | Directly runnable |
| Execute an actual MR against an original program and mutant | `python3 scripts/demo_tsq.py` | Directly runnable |
| Inspect the programs, MRs, test cases, and mutants | `code/`, `data/`, and `docs/` | Directly available |
| Reanalyze final technique, variant, and statistical results | `results/` | Directly available |
| Rerun the complete execution and coverage pipeline | Subject drivers under `code/` | Requires configuration and regenerated intermediates |

Per-execution coverage traces and intermediate spectrum data are generated
artifacts and are not stored in this repository because the original generated
workspace is approximately 25 GB. The scripts that produced them are retained
for traceability, but some preserve machine-specific paths from the original
experimental environment. The repository therefore does not claim a portable
one-command rerun of the complete experiment.

## Implementation Map

The shared implementation is in [`publicFun.py`](publicFun.py):

| Component | Functions | Role |
| --- | --- | --- |
| Risk formulas | `riskformula`, `riskformula2` | Calculate suspiciousness using the 30 evaluated formulas |
| MG spectrum without FRI | `Sus`, `Sus_grep` | Use an MG as the test entity and union its test-case coverage |
| MG spectrum with FRI | `FaSus`, `FaSus_grep` | Refine an MR-violating MG using the topmost test case identified by FAILTIM |
| Test-case spectrum with FRI | `SBFLSus`, `SBFLSus_grep` | Construct test-case-level spectrum information using FAILTIM |
| Weighted variants | `FaflVariantSus*` | Vary the contribution of topmost and non-topmost test cases |
| Evaluation | `Exam`, `TopN` | Calculate EXAM and TOP-N effectiveness |

The code and workbook columns retain historical internal labels such as `MS`,
`FA`, `PS`, and `FAFL` for traceability to the original experiment. See
[`code/README.md`](code/README.md) for the behavior represented by these
functions and labels rather than relying on the legacy names alone.

## Results and Analyses

The final workbooks are:

- [`results/all-techniques.xlsx`](results/all-techniques.xlsx), containing
  per-subject, per-mutant, and per-formula results together with aggregate
  technique and variant summaries; and
- [`results/statistical-tests.xlsx`](results/statistical-tests.xlsx),
  containing pairwise Wilcoxon Signed-Rank test results for technique and
  risk-formula comparisons.

The worksheet-level mapping is documented in
[`results/README.md`](results/README.md). For the technique comparisons, the
unit of analysis in the Wilcoxon Signed-Rank test is a mutant. For each mutant,
technique, and evaluation metric, the results over the 30 risk formulas are
averaged; the two mutant-level values for a pair of techniques form one paired
observation.

## Known Packaging Gap

The recovered source workspace does not contain the source directories for six
selected Grep versions (`grep_v51` through `grep_v56`). Their mutant identifiers
and faulty source-line locations were recovered from the preserved experiment
driver, but the exact source-code replacements have not been reconstructed.
The final experimental results still include these versions. This known gap is
reported by the inventory checker and documented in
[`docs/MUTANTS.md`](docs/MUTANTS.md#packaging-status); it is not silently
replaced with inferred source code.

## Citation and Contact

Please cite the accompanying paper when using this replication package. For
questions about the artifacts, open an issue in this repository or contact
`rendaixu@tiangong.edu.au`.
