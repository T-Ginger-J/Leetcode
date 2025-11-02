# LeetCode 193: Valid Phone Numbers (Python Equivalent)
# Explanation:
# 1. Use regex to validate each line in a file.
# 2. Match same patterns as Bash version.
# Time Complexity: O(n)
# Space Complexity: O(1)

import re

pattern = re.compile(r'^(\(\d{3}\)\s|\d{3}-)\d{3}-\d{4}$')
with open("file.txt", "r") as f:
    for line in f:
        if pattern.match(line.strip()):
            print(line.strip())
