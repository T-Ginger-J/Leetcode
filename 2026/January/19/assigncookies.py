# LeetCode 455: Assign Cookies
# Explanation:
# Each child has a greed factor g[i], and each cookie has a size s[j].
# A child is content if s[j] >= g[i].
# Each cookie can be assigned to at most one child.
# Goal: maximize the number of content children.
#
# Method 1: Greedy with Sorting (Optimal)
# - Sort both greed factors and cookie sizes.
# - Use two pointers:
#     - If current cookie satisfies current child, assign it.
#     - Otherwise, try a larger cookie.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) (ignoring sort cost)

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        content = 0

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                content += 1
                i += 1
                j += 1
            else:
                j += 1

        return content


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: More cookies than children
print(sol.findContentChildren([1,2], [1,2,3]))
# Expected output: 2

# Example 2: Not enough cookie sizes
print(sol.findContentChildren([1,2,3], [1]))
# Expected output: 1

# Example 3: Exact matches required
print(sol.findContentChildren([2,3,4], [1,2,3]))
# Expected output: 2
