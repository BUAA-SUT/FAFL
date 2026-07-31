grep -E -n "\b[a-zA-Z0-9]+\b" ./../partition_scheme_testcases_1.2 >> MR5

grep -E -o "\b[a-zA-Z0-9]+\b" ./../partition_scheme_testcases_1.2 >> MR5_matched_content
