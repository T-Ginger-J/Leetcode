# LeetCode 433: Minimum Genetic Mutation
# Explanation:
# 1. Use BFS to find the shortest path from start to end, changing one character at a time.
# 2. Only valid mutations in the bank are allowed.
# 3. Track visited sequences to avoid cycles.

from collections import deque

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank_set = set(bank)
        if end not in bank_set:
            return -1
        
        genes = ['A', 'C', 'G', 'T']
        queue = deque([(start, 0)])
        visited = set([start])
        
        while queue:
            current, steps = queue.popleft()
            if current == end:
                return steps
            
            # Try all possible single-character mutations
            for i in range(len(current)):
                for g in genes:
                    if current[i] == g:
                        continue
                    mutation = current[:i] + g + current[i+1:]
                    if mutation in bank_set and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, steps + 1))
        
        return -1

# Example 1
start = "AACCGGTT"
end = "AACCGGTA"
bank = ["AACCGGTA"]
# Output: 1
print(Solution().minMutation(start, end, bank))

# Example 2
start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# Output: 2
print(Solution().minMutation(start, end, bank))

# Example 3
start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# Output: 3
print(Solution().minMutation(start, end, bank))
