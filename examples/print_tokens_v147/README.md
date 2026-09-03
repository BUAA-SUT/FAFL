# Partial FAILTIM Illustration: `print_tokens_v147`

This supplementary case uses a real mutant and test pair preserved from the PT
experimental workspace. It illustrates how FAILTIM identifies the topmost test
case in an MR-violating metamorphic group (MG), and how that identification
determines the coverage information retained by an FRI-based MG technique.

This is a **partial illustration**, not a complete end-to-end comparison of the
four MFL techniques. A final program-element ranking is calculated from all
relevant MGs, their spectrum information, and a selected risk formula. The
controlled example in Section 3.3.3 of the paper is therefore retained for the
complete comparison.

## Mutant

The case concerns `printtokens_v147` from the Print_tokens (PT) benchmark. It
changes Line 231 of `print_tokens.c` as follows:

```diff
- token_ptr->token_id=keyword(next_st);
+ token_ptr->token_id=keyword(-next_st);
```

The complete one-line patch is provided in [`mutation.patch`](mutation.patch).
It applies to the original PT source at
[`code/PT/print_tokens.c`](../../code/PT/print_tokens.c).

## MR1 test pair

PT's MR1 swaps the letter case of selected input lines. Because this source
test case contains one line, MR1 swaps the case of the complete line:

| Role | Repository file | Input |
| --- | --- | --- |
| Source test case, `t_s` | [`source.txt`](source.txt) | ``if i ` ;nd5 ;YfI8`` |
| Follow-up test case, `t_f` | [`follow-up.txt`](follow-up.txt) | ``IF I ` ;ND5 ;yFi8`` |

For the original program, both executions contain two tokens in the combined
identifier-or-keyword category, so the MG satisfies MR1. For
`printtokens_v147`, the source execution produces `error`, whereas the
follow-up execution still produces the expected two identifier tokens. The MG
therefore violates MR1.

## FAILTIM identification

The original program supplies ground-truth outputs only for experimental
validation; these outputs are not inputs to FAILTIM or to the MFL techniques.
They establish that `t_s` is the actual failure-revealing test case and `t_f`
is non-failure-revealing.

FAILTIM calculates test-case suspiciousness from observable MR outcomes. The
experiments consistently use the **Arithmetic Mean** risk formula for this
test-case identification step. For this pair, the recorded scores are:

| Test case | FAILTIM score | Identification |
| --- | ---: | --- |
| `t_s` | 0.5926 | Topmost test case |
| `t_f` | -0.4444 | Non-topmost test case |

Thus, FAILTIM correctly identifies the source test case without using its
ground-truth output.

## Coverage consequence

The preserved statement-coverage table shows that Line 231 is covered by
`t_s` but not by `t_f`. An FRI-based MG technique that retains the coverage of
the topmost test case therefore retains the faulty statement in the spectrum
column for this MR-violating MG.

The scores and the two coverage entries extracted for this example are retained
in [`case-data.csv`](case-data.csv). The source and follow-up inputs are also
the packaged `input0` and `input0_0` entries in
[`data/PT/RandomInput.csv`](../../data/PT/RandomInput.csv).

This local observation does not by itself determine the final fault-localization
ranking. That ranking also depends on the spectrum information contributed by
the other MGs and on the program-element risk formula.

## Reproduce the observable part

Run the following command from the repository root:

```bash
python3 examples/print_tokens_v147/verify_example.py
```

The script builds the original program and the mutant in a temporary directory,
runs both test cases, checks their MR1 outcomes, and verifies the recorded
inputs and coverage difference at Line 231. Reproducing the two FAILTIM scores
requires the complete MG context used by FAILTIM and is outside this partial
example.
