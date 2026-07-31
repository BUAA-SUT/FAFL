grep -E -vn "\w+-\w+" ./../normal_literals > normal_literals_4_MR10
sed -e '/NULL/d' ./normal_literals_4_MR10 > normal_literals_4_MR10_lines
