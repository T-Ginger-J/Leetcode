#!/bin/bash
# LeetCode 194: Transpose File
# Explanation:
# 1. Read each line and split by space into words.
# 2. Append each word to its corresponding line number in an array.
# 3. Print accumulated columns.
# Time Complexity: O(n * m)  (n = rows, m = columns)
# Space Complexity: O(n * m)

awk '
{
  for (i = 1; i <= NF; i++) {
    if (NR == 1) {
      s[i] = $i
    } else {
      s[i] = s[i]" "$i
    }
  }
}
END {
  for (i = 1; i <= NF; i++) print s[i]
}' file.txt
