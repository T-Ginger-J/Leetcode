# LeetCode 388: Longest Absolute File Path
# Explanation:
# 1. Track path lengths by depth using a dict
# 2. Update max_len when a file is found
# Time Complexity: O(n)
# Space Complexity: O(depth)

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_len = 0
        path_len = {0: 0}  # depth 0 has length 0
        for line in input.split('\n'):
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1  # +1 for '/'
        return max_len

