# Selected Mutants

The experiments use 114 single-fault versions. Mutants that could not be
compiled or that produced no MR violation under the available MRs and test
cases were excluded before fault localization.

Both filtering conditions are observable during the experiment. Compilation
failure is reported by the build process, and MR violation is determined by
checking the source and follow-up outputs against the corresponding MR; neither
step requires an individual test oracle.

## Mutant Inventory

| Subject | Selected mutant identifiers | Count |
| --- | --- | ---: |
| TSQ | 1-5 | 5 |
| DM | 1-5 | 5 |
| SMM | 2-7 | 6 |
| KNN | 1, 2, 4 | 3 |
| Tcas | 1-20 | 20 |
| PT | 2, 32, 58, 88, 120, 134, 161, 201, 202, 205, 210, 215, 220, 240, 260, 354, 355, 360, 364, 366, 368 | 21 |
| PT2 | 1-21 | 21 |
| Grep | 5, 10-14, 16, 18, 20, 23, 25-27, 29-31, 34-36, 38-41, 43, 46, 49-56 | 33 |

## Source Locations

- Python mutants are stored as individual modules under
  `code/<subject>/mutants/`.
- Tcas stores the twenty mutant classes in
  `code/Tcas/mutants/Mutants.py`.
- PT and PT2 store each selected C version in its own directory under
  `code/PT/mutants/` and `code/PT2/mutants/`.
- Grep stores each available C version in its own directory under
  `code/Grep/mutants/`.
