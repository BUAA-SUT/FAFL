grep -E -n "\(\[\w*\]\)|^\[\w*\]$" ./../input > MR3

grep -E -o "\(\[\w*\]\)|^\[\w*\]$" ./../input > MR3_matched_content
