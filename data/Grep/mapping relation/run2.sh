grep -E -n "\[\w+-\w+\]" ./input > MR1Relation/MR1
grep -E -o "\[\w+-\w+\]" ./input > MR1Relation/MR1_matched_content

grep -E -n "\(\[\w*-\w*\]\)" ./input > MR2Relation/MR2
grep -E -o "\(\[\w*-\w*\]\)" ./input > MR2Relation/MR2_matched_content

grep -E -n "\(\[\w*\]\)|^\[\w*\]$" ./input > MR3Relation/MR3
grep -E -o "\(\[\w*\]\)|^\[\w*\]$" ./input > MR3Relation/MR3_matched_content

grep -E -n "\[\w+-\w+\]" ./input > MR4Relation/MR4_relation

grep -E -nv "\|$" ./input > MR9Relation/MR9

grep -E -vn "\w+-\w+" ./normal_literals > MR10Relation/normal_literals_4_MR10
sed -e '/NULL/d' MR10Relation/normal_literals_4_MR10 > MR10Relation/normal_literals_4_MR10_lines
