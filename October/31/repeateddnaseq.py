# LeetCode 187: Repeated DNA Sequences
# Explanation:
# 1. Use a sliding window of size 10 to extract substrings.
# 2. Keep track of seen substrings in a set.
# 3. If a substring is seen again, add it to the repeated set.
# 4. Return all repeated substrings as a list.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)
