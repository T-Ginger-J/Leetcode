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

