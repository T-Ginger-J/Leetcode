from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return []
        
        p_count = Counter(p)
        window_count = Counter()
        result = []
        
        for i in range(len_s):
            window_count[s[i]] += 1
            if i >= len_p:
                # Remove leftmost character from window
                left_char = s[i - len_p]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1
            
            if window_count == p_count:
                result.append(i - len_p + 1)
        
        return result

