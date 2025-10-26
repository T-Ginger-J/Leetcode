# LeetCode 165: Compare Version Numbers
# Explanation:
# 1. Split both version strings by '.' to get numeric parts.
# 2. Convert each part to integer for numerical comparison.
# 3. Pad the shorter version with zeros so both have equal length.
# 4. Compare each corresponding part:
#    - If part1 > part2 → return 1
#    - If part1 < part2 → return -1
#    - Else continue
# 5. Return 0 if all parts are equal.
# Time Complexity: O(n) where n = max(len(version1), len(version2))
# Space Complexity: O(n)

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n = max(len(v1), len(v2))
        v1 += [0] * (n - len(v1))
        v2 += [0] * (n - len(v2))
        for a, b in zip(v1, v2):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0
