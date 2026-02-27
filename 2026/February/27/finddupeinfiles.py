# LeetCode 609: Find Duplicate File in System
# Explanation:
# 1. Each input string represents a directory followed by files with content.
#    Format: "root/a 1.txt(abcd) 2.txt(efgh)"
# 2. Files are considered duplicates if their contents are identical.
# 3. Parse each string:
#    - First token is the directory path.
#    - Remaining tokens are files: name(content).
# 4. Map file content -> list of full file paths.
# 5. Return only groups with more than one file.
#
# Method 1 (Hash Map Parsing):
# - Use a dictionary: content -> [paths].
# - Iterate through all paths and files.
# - Build full path = dir + "/" + filename.
#
# Time Complexity: O(N * L)
#   N = number of files, L = average length of each file string.
# Space Complexity: O(N * L)
#   For storing paths and contents.
#
# Alternative Method 1 (Using defaultdict):
# - Same logic, cleaner grouping using collections.defaultdict(list).
#
# Alternative Method 2 (Regex Parsing):
# - Use regex to extract filename and content.
# - Useful if format becomes more complex.
# - Same asymptotic complexity.


from typing import List
from collections import defaultdict
import re


class Solution:

    # Main Solution: Hash Map Parsing
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = defaultdict(list)

        for entry in paths:
            parts = entry.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name, content = file_info.split("(")
                content = content[:-1]  # remove ')'

                full_path = directory + "/" + name
                content_map[content].append(full_path)

        return [v for v in content_map.values() if len(v) > 1]


