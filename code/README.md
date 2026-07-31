# Experiment Code

Each subject directory contains its program implementation or execution
harness, MR implementation, original experiment driver, and selected mutants.
PT, PT2, and Grep additionally contain subject-specific execution and
statement-coverage utilities.

## Shared Implementation

The common spectrum construction, suspiciousness calculation, and evaluation
code is in [`../publicFun.py`](../publicFun.py).

| Function family | Implementation role |
| --- | --- |
| `riskformula*` | The 30 evaluated risk formulas |
| `Sus*` | MG-based spectrum using union coverage without additional FRI |
| `FaSus*` | MG-based spectrum refined using the topmost test case from FAILTIM |
| `SBFLSus*` | Test-case-level spectrum constructed using FAILTIM |
| `FaflSus*`, `MmSus*` | Additional historical experimental configurations |
| `FaflVariantSus*` | Weighted variants of the FRI-based MG construction |
| `SBFL*` | Oracle-based SBFL reference used in the original analysis |
| `Exam`, `TopN` | Fault-localization effectiveness metrics |
| `getMetrics_*` | Workbook-row construction for the experiment outputs |

Function suffixes ending in `_grep` adapt the same calculations to the Grep
data representation.

## Historical Labels

The implementation predates the final terminology used in the paper. As a
result, drivers and result workbooks retain internal labels such as `MS`, `FA`,
`PS`, `FAFL`, and `MM`. These names are preserved so that the source code can be
traced to the recorded workbooks. The relevant behavior is defined by the
spectrum construction performed in `publicFun.py`; the internal label alone
should not be treated as a formal technique definition.

The clearest entry points are:

- `Sus`: an MG is the test entity and coverage is the union of all test cases
  in that MG;
- `FaSus`: for an MR-violating MG, FAILTIM ranks the constituent test cases and
  the topmost test case is used to refine its coverage information;
- `SBFLSus`: individual test cases are represented in the spectrum and FAILTIM
  supplies the failure-revealing identification; and
- `FaflVariantSus*`: the assignment weights are varied to analyze the
  contribution of topmost and non-topmost test cases.

## Subject Drivers

| Subject | MR implementation | Original driver |
| --- | --- | --- |
| TSQ | `TSQ/TSQ.py` | `TSQ/TSQ_test.py` |
| DM | `DM/DM.py` | `DM/DM_test.py` |
| SMM | `SMM/SMM.py` | `SMM/SMM_test.py` |
| KNN | `KNN/KNN.py` | `KNN/KNN_test.py` |
| Tcas | `Tcas/Tcas.py` | `Tcas/Tcas_test.py` |
| PT | `PT/PT.py` | `PT/PT_test.py` |
| PT2 | `PT2/PT2.py` | `PT2/PT2_test.py` |
| Grep | `Grep/MRs/MR.py` | `Grep/test_grep.py` |

The original drivers require generated execution/coverage data and retain some
absolute paths from the research environment. They are provided for
traceability and are not portable one-command runners. Start with the runnable
[`../scripts/demo_tsq.py`](../scripts/demo_tsq.py) example, then consult
[`../docs/REPRODUCIBILITY.md`](../docs/REPRODUCIBILITY.md) before configuring a
complete rerun.

See also:

- [`../docs/SUBJECTS.md`](../docs/SUBJECTS.md) for the artifact map;
- [`../docs/METAMORPHIC_RELATIONS.md`](../docs/METAMORPHIC_RELATIONS.md) for MR
  semantics; and
- [`../docs/MUTANTS.md`](../docs/MUTANTS.md) for mutant identifiers and
  packaging status.
