# LeetCode 599: Minimum Index Sum of Two Lists
# Explanation:
# 1. We are given two lists of strings.
# 2. We want common strings with the smallest index sum.
# 3. Approach:
#    - Store list1 elements with their indices in a hash map.
#    - Traverse list2 and check if element exists in map.
#    - Track minimum index sum.
#    - Collect all strings with that minimum sum.
# 4. Time Complexity: O(n + m)
# 5. Space Complexity: O(n)

from typing import List


class Solution:

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index_map = {}

        # Store indices of list1
        for i, name in enumerate(list1):
            index_map[name] = i

        best = float("inf")
        res = []

        # Traverse list2
        for j, name in enumerate(list2):

            if name in index_map:

                s = index_map[name] + j

                if s < best:
                    best = s
                    res = [name]

                elif s == best:
                    res.append(name)

        return res

