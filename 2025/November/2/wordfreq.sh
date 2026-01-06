#!/bin/bash
# LeetCode 192: Word Frequency
# Explanation:
# Use Unix tools: tr, sort, uniq, awk to count word frequencies and sort descending.
# Time Complexity: O(n log n) (due to sort)
# Space Complexity: O(n)

cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -rn | awk '{ print $2, $1 }'
