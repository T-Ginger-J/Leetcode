#!/bin/bash
# LeetCode 195: Tenth Line
# Explanation:
# 1. Use `sed` to print only the 10th line.
# 2. The `-n` suppresses automatic printing; `10p` prints only line 10.
# Time Complexity: O(n)
# Space Complexity: O(1)

sed -n '10p' file.txt
