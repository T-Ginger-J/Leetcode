from typing import Optional, List
from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = defaultdict(int)
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0
            s = dfs(node.left) + dfs(node.right) + node.val
            freq[s] += 1
            max_freq = max(max_freq, freq[s])
            return s

        dfs(root)
        return [s for s, c in freq.items() if c == max_freq]
