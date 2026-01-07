# LeetCode 406: Queue Reconstruction by Height
# Explanation:
# 1. Sort by descending height, ascending k
# 2. Insert each person at index=k
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for person in people:
            res.insert(person[1], person)
        return res
