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

input1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(Solution().lengthLongestPath(input1))  # Output: 20 ("dir/subdir2/file.ext")

input2 = "a"
print(Solution().lengthLongestPath(input2))  # Output: 0 (no file)
