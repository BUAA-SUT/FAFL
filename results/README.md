# Experimental Results

The two workbooks in this directory preserve the final results and statistical
comparisons used in the study. They can be inspected independently of the
large per-execution coverage workspace.

## `all-techniques.xlsx`

| Worksheet | Contents |
| --- | --- |
| `TSQ`, `DM`, `SMM`, `KNN`, `Tcas`, `PT`, `PT2`, `grep` | Per-mutant and per-risk-formula results for EXAM and TOP-1/3/5/10, plus diagnostic columns recorded during the experiments |
| `result` | Aggregate comparison of the evaluated technique configurations |
| `result-1` | Aggregate comparison of the weighted variants |
| `Sheet1` | Preserved worksheet from the original analysis workbook |

The subject worksheets contain one row for each mutant/formula combination.
The `MS`, `FA`, `PS`, `FAFL`, `MM`, and `SBFL` column prefixes are historical
internal labels retained from the experiment code. Their behavior should be
interpreted together with [`../code/README.md`](../code/README.md) and
[`../publicFun.py`](../publicFun.py).

The diagnostic columns include `SMG`, `FS`, `WrongP`, `pot`, `pof`, `pal`, and
`StaDe`, where present. They support the analyses of MR-satisfying/violating
groups, FAILTIM identification, and related result characteristics. Their exact
construction is retained in the `getMetrics_*` functions in `publicFun.py`.

## `statistical-tests.xlsx`

| Worksheets | Contents |
| --- | --- |
| `method-EXAM`, `method-TOP-1`, `method-TOP-3`, `method-TOP-5`, `method-TOP-10` | Pairwise technique comparisons for each evaluation metric |
| `EXAM`, `TOP-1`, `TOP-3`, `TOP-5`, `TOP-10` | Pairwise risk-formula comparisons for each evaluation metric |

The unit of analysis in the Wilcoxon Signed-Rank technique comparisons is a
mutant. For each mutant, technique, and evaluation metric, results are averaged
over the 30 risk formulas. The two averages for the same mutant form one paired
observation, and the test is conducted separately for each metric.

## Analysis Map

| Study analysis | Primary workbook location |
| --- | --- |
| Comparison of the representative MFL techniques | `all-techniques.xlsx`: subject sheets and `result`; `statistical-tests.xlsx`: `method-*` |
| Comparison of the 30 risk formulas | `all-techniques.xlsx`: subject sheets; `statistical-tests.xlsx`: metric-named sheets |
| Analysis of the weighted technique variants | `all-techniques.xlsx`: `result-1` |
| FAILTIM and false-satisfaction supporting data | Diagnostic columns in the subject and aggregate sheets |

The workbooks contain final analysis data rather than the omitted
per-execution coverage traces. See
[`../docs/REPRODUCIBILITY.md`](../docs/REPRODUCIBILITY.md) for the distinction
between packaged results and generated intermediate data.
