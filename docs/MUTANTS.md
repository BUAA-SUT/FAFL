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

## Packaging Status

The supplied local source workspace contains Grep mutant directories through
`grep_v50`. The experiment and result data also refer to selected mutants
`grep_v51` through `grep_v56`, but their source directories were not present in
the supplied workspace. These six versions were added in a later STVR-related
extension of the Grep experiment. The preserved experiment driver and result
files identify their faulty source lines and the corresponding zero-based
positions in the 3,661-element executable-statement vector:

| Mutant | Faulty source line | Nonzero position in `Flag` |
| --- | ---: | ---: |
| `grep_v51` | 7156 | 1990 |
| `grep_v52` | 1729 | 572 |
| `grep_v53` | 7163 | 1995 |
| `grep_v54` | 8708 | 2720 |
| `grep_v55` | 8003 | 2385 |
| `grep_v56` | 7142 | 1980 |

The source-line mapping is retained in `code/Grep/test_grep.py`, and the
nonzero `Flag` positions were verified against the original
`mutant51.json`-`mutant56.json` result files. These records establish the
fault locations, but they do not record the exact source-code replacement made
at each location. The package therefore includes the other 27 selected Grep
source versions and does not fabricate source directories for `grep_v51`
through `grep_v56`. Those directories or equivalent mutation records must be
recovered before the source package can be described as complete for all 114
mutants.
