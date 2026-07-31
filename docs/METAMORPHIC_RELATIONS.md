# Metamorphic-Relation Specifications

The study uses 88 MRs. The executable definitions are authoritative: they
generate the follow-up test cases and determine whether the source and follow-up
outputs satisfy or violate each MR. This document provides a compact semantic
index to those implementations.

## TSQ: 9 MRs

Source: `code/TSQ/TSQ.py`

For a source triangle with sides `(a, b, c)`, MR1-MR3 replace one side using a
parallelogram-law expression; MR4-MR9 compose two such transformations. In all
nine cases, the expected relation is equality of the source and follow-up
triangle areas, compared to four decimal places.

## DM: 10 MRs

Source: `code/DM/DM.py`

| MR | Input transformation | Expected output relation |
| --- | --- | --- |
| MR1 | Exchange two rows | Follow-up determinant is the negation of the source determinant |
| MR2 | Subtract three times one row from another | Determinant is unchanged |
| MR3 | Transpose the matrix | Determinant is unchanged |
| MR4 | Invert the matrix | Product of source and follow-up determinants is 1 |
| MR5 | MR1 followed by MR2 | Determinant is negated |
| MR6 | MR2 followed by MR1 | Determinant is negated |
| MR7 | MR1 followed by MR3 | Determinant is negated |
| MR8 | MR3 followed by MR1 | Determinant is negated |
| MR9 | MR2 followed by MR3 | Determinant is unchanged |
| MR10 | MR3 followed by MR2 | Determinant is unchanged |

## SMM: 15 MRs

Source: `code/SMM/SMM.py`

| MR | Input transformation | Expected output relation |
| --- | --- | --- |
| MR1 | `(A, B)` to `(B^T, A^T)` | Follow-up output is `(AB)^T` |
| MR2 | Premultiply `A` by a permutation matrix `P` | Follow-up output is `P(AB)` |
| MR3 | Postmultiply `B` by `P` | Follow-up output is `(AB)P` |
| MR4 | Premultiply `A` by another permutation matrix `Q` | Follow-up output is `Q(AB)` |
| MR5 | Postmultiply `B` by `Q` | Follow-up output is `(AB)Q` |
| MR6 | Multiply `A` by 6 | Follow-up output is `6(AB)` |
| MR7 | Multiply `B` by 7 | Follow-up output is `7(AB)` |
| MR8 | Replace `A` with `A + I` | Follow-up output is `AB + B` |
| MR9 | Replace `B` with `B + I` | Follow-up output is `A + AB` |
| MR10-MR15 | Ordered compositions of MR1-MR3 | Composition of the corresponding output transformations |

## KNN: 11 MRs

Source: `code/KNN/KNN.py`

| MR | Input transformation | Expected output relation |
| --- | --- | --- |
| MR1 | Apply the same affine transformation to every non-label attribute in the training and test sets | Predicted labels are unchanged |
| MR2 | Apply the same attribute permutation to the training and test sets | Predicted labels are unchanged |
| MR3 | Add repeated copies of the test sample, labeled with its source prediction, to the training set | Prediction is unchanged |
| MR4 | Add a training sample whose class equals the source prediction | Prediction is unchanged |
| MR5 | Split non-predicted classes by relabeling selected training samples | Prediction is unchanged |
| MR6-MR11 | Ordered compositions of MR1-MR3 | Prediction is unchanged |

## Tcas: 9 MRs

Source: `code/Tcas/Tcas.py`

MR1-MR3 alter altitude-separation fields, upward-separation fields, and
altitude-layer values according to the source advisory. MR4-MR9 apply ordered
compositions of these three transformations. Every applicable MR expects the
advisory (`UPWARD_RA`, `DOWNWARD_RA`, or `UNRESOLVED`) to remain unchanged.
The implementation returns a distinct value when a source input does not admit
the requested transformation.

## PT and PT2: 11 MRs Each

Sources: `code/PT/PT.py` and `code/PT2/PT2.py`

| MR | Input transformation | Expected output relation |
| --- | --- | --- |
| MR1 | Swap the letter case of 50% of input lines | Token-count vector is unchanged |
| MR2 | Remove content after the first unquoted semicolon on each applicable line | Token-count vector is unchanged |
| MR3 | Prefix 50% of input lines with a semicolon | No token count may increase |
| MR4 | MR1 followed by MR2 | Token-count vector is unchanged |
| MR5 | MR2 followed by MR1 | Token-count vector is unchanged |
| MR6 | MR1 followed by MR3 | No token count may increase |
| MR7 | MR3 followed by MR1 | No token count may increase |
| MR8 | MR2 followed by MR3 | No token count may increase |
| MR9 | MR3 followed by MR2 | No token count may increase |
| MR10 | Duplicate 10% of input lines | No token count may decrease |
| MR11 | Remove 10% of input lines | No token count may increase |

## Grep: 12 MRs

Source: `code/Grep/MRs/MR.py`

| MR | Regular-expression transformation | Expected output relation |
| --- | --- | --- |
| MR1 | Replace a character range with a shuffled explicit character collection | Outputs are equal |
| MR2 | Replace a character range with an alternation of its characters | Outputs are equal |
| MR3 | Replace a character collection with an alternation of singleton collections | Outputs are equal |
| MR4 | Split a character range into two adjacent subranges | Outputs are equal |
| MR5 | Shuffle characters and form a character collection | Source matches are contained in follow-up matches |
| MR6 | Shuffle characters and form an alternation | Source matches are contained in follow-up matches |
| MR7 | Remove the upper endpoint from a character range | Follow-up matches are contained in source matches |
| MR8 | Extend a character range by one character | Source matches are contained in follow-up matches |
| MR9 | Add a digit-class alternative | Relation is checked using the MR9 target-file procedure |
| MR10 | Append an identity-preserving quantifier to a selected literal | Outputs are equal |
| MR11 | Replace a character class by its complement | Relation is checked using the MR11 target-file procedure |
| MR12 | Replace selected literal characters with dot wildcards | Source matches are contained in follow-up matches |

## MG Size in the Current Experiments

Every MR used in the reported experiments generates one follow-up test case
from one source test case. Each experimental MG therefore contains two test
cases. This is a property of the selected MR implementations, not a restriction
of the MFL framework.
