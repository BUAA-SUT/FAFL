# Subject Programs and Packaged Artifacts

This document maps each subject reported in the paper to its implementation,
MR definitions, source test cases, and selected mutants.

## Artifact Map

| Subject | Main MR implementation | Experiment driver | Source-test data | Mutant source |
| --- | --- | --- | --- | --- |
| TSQ | `code/TSQ/TSQ.py` | `code/TSQ/TSQ_test.py` | `data/TSQ/source-test-cases.json` | `code/TSQ/mutants/` |
| DM | `code/DM/DM.py` | `code/DM/DM_test.py` | `data/DM/source-test-cases.json` | `code/DM/mutants/` |
| SMM | `code/SMM/SMM.py` | `code/SMM/SMM_test.py` | `data/SMM/source-test-cases.json` | `code/SMM/mutants/` |
| KNN | `code/KNN/KNN.py` | `code/KNN/KNN_test.py` | `data/KNN/source-test-cases.json` and `data/KNN/iris.data` | `code/KNN/mutants/` |
| Tcas | `code/Tcas/Tcas.py` | `code/Tcas/Tcas_test.py` | `data/Tcas/source-test-cases.json` and `data/Tcas/universe.txt` | `code/Tcas/mutants/` |
| PT | `code/PT/PT.py` | `code/PT/PT_test.py` | `data/PT/RandomInput.csv` | `code/PT/mutants/` |
| PT2 | `code/PT2/PT2.py` | `code/PT2/PT2_test.py` | `data/PT2/RandomInput.csv` | `code/PT2/mutants/` |
| Grep | `code/Grep/MRs/MR.py` | `code/Grep/test_grep.py` | `data/Grep/RandomInput.csv` and supporting files under `data/Grep/` | `code/Grep/mutants/` |

## Subject Notes

### TSQ

TSQ computes the area of a triangle. Each source test case is a triple of side
lengths. The nine MRs construct new triples whose areas should equal the source
area. The Python mutant classes are packaged separately so that each faulty
version can be selected by the driver.

### DM

DM calculates a matrix determinant. Its ten MRs use row exchange, row
replacement, transposition, inversion, and compositions of these
transformations. The expected determinant is unchanged, negated, or reciprocal,
depending on the transformation.

### SMM

SMM performs square-matrix multiplication. Its fifteen MRs use transposition,
row/column permutations, scaling, identity-matrix addition, and compositions of
the basic transformations.

### KNN

KNN is a k-nearest-neighbor classifier. Its eleven MRs transform feature
values, permute attributes, add or relabel training samples, and compose these
operations while preserving the expected classification.

### Tcas

Tcas is an aircraft collision-avoidance program. The Python harness implements
nine output-preserving MRs over the TCAS input vector. `Mutants.py` contains the
twenty selected faulty implementations.

### PT and PT2

PT and PT2 are token-counting programs. Their eleven MRs transform input lines
through case changes, semicolon-related truncation or prefixing, MR
compositions, duplication, and deletion. The expected relation is expressed
over token-count vectors.

### Grep

Grep is driven through regular-expression transformations. Its twelve MRs
rewrite equivalent character ranges or collections, narrow or expand matched
sets, add alternatives, and transform literals. Some MRs require target files
or mapping data; these supporting artifacts are under `data/Grep/`.

## Generated Artifacts

The original experiment workspace also contains generated MR outcomes,
statement-coverage traces, spectrum matrices, and intermediate JSON files.
These artifacts are not source inputs and are not required for understanding
the MR or mutant definitions. They are intentionally excluded from the GitHub
package because they account for most of the approximately 25 GB workspace.
