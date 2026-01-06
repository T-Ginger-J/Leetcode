# LeetCode 133: Clone Graph
# Explanation:
# 1. Each node has neighbors, forming an undirected graph.
# 2. We use DFS or BFS to clone every node and its neighbors.
# 3. Maintain a hashmap mapping original nodes to cloned ones to prevent duplicates.
# Time Complexity: O(V + E), where V = number of nodes, E = number of edges.
# Space Complexity: O(V)

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        old_to_new = {}

        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            clone = Node(n.val)
            old_to_new[n] = clone
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)

    def cloneGraphBFS(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    queue.append(nei)
                clones[curr].neighbors.append(clones[nei])
        return clones[node]

# Graph: 1--2
#        |  |
#        4--3
n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2, n4]
n2.neighbors = [n1, n3]
n3.neighbors = [n2, n4]
n4.neighbors = [n1, n3]

clone = Solution().cloneGraph(n1)
print(clone.val)            # Output: 1
print([n.val for n in clone.neighbors])  # Output: [2, 4]
