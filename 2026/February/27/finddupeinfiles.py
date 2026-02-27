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


