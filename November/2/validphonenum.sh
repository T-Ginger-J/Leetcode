#!/bin/bash
# LeetCode 193: Valid Phone Numbers
# Explanation:
# 1. Use grep with regex to match valid phone number formats:
#    - ^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$   → (xxx) xxx-xxxx
#    - ^[0-9]{3}-[0-9]{3}-[0-9]{4}$       → xxx-xxx-xxxx
# 2. Anchors ^ and $ ensure the pattern matches the entire line.
# Time Complexity: O(n)
# Space Complexity: O(1)

grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
