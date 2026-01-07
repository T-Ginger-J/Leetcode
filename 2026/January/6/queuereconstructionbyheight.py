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

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(Solution().reconstructQueue(people))
# Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
