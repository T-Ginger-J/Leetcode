class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        # Sort by height descending, k ascending
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for person in people:
            res.insert(person[1], person)
        return res
