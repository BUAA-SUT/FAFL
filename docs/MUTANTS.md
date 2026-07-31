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

All 114 selected mutant sources are included. Grep versions 51-56 were
recovered from the later Grep extension workspace by matching the faulty-line
positions preserved in `test_grep.py` with the mutation descriptions in the
original mutant directories. They are stored with the other selected versions
under `code/Grep/mutants/`.

| Published version | Recovered source | Line | Original expression | Mutated expression |
| --- | --- | ---: | --- | --- |
| `grep_v51` | extension `grep_v1` | 7156 | `RE_NO_BK_PARENS) == 0` | `RE_NO_BK_PARENS) != 0` |
| `grep_v52` | extension `grep_v7` | 1729 | `nfirstpos[-1]` | `nfirstpos[+1]` |
| `grep_v53` | extension `grep_v9` | 7163 | `RE_NO_BK_PARENS) == 0` | `RE_NO_BK_PARENS) != 0` |
| `grep_v54` | extension `grep_v10` | 8708 | `malloc(newsize + 1)` | `malloc(newsize - 1)` |
| `grep_v55` | extension `grep_v11` | 8003 | `d->follows[i].nelem < merged.nelem` | `d->follows[i].nelem > merged.nelem` |
| `grep_v56` | extension `grep_v13` | 7142 | `RE_NO_BK_VBAR) == 0` | `RE_NO_BK_VBAR) != 0` |

The corresponding `ReadMe` file in each directory preserves the complete
mutation record and provenance. The line numbers also match the six `Flag`
assignments in the original experiment driver, so these versions are recovered
artifacts rather than inferred or newly generated mutants.
