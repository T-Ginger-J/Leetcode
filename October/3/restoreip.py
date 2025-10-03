# LeetCode 93: Restore IP Addresses
# Explanation:
# 1. We must insert 3 dots in the string to form 4 valid segments.
# 2. Each segment must be:
#    - Between 0 and 255
#    - No leading zeros unless the segment is exactly "0".
# 3. Use backtracking:
#    - At each step, choose a segment of length 1 to 3.
#    - If valid, recurse on remaining string and segment count.
#    - Stop when 4 segments are formed and string is consumed.
# Time Complexity: O(3^4) = O(81) ≈ O(1) since max 12 chars.
# Space Complexity: O(1) excluding result storage.

from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        
        def backtrack(start, path):
            if start == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            if len(path) >= 4:
                return
            
            for length in range(1, 4):
                if start + length > len(s):
                    break
                seg = s[start:start+length]
                if (seg.startswith("0") and len(seg) > 1) or int(seg) > 255:
                    continue
                backtrack(start+length, path+[seg])
        
        backtrack(0, [])
        return res

    def restoreIpAddressesPruning(self, s: str) -> List[str]:
        def valid(seg): 
            return str(int(seg)) == seg and 0 <= int(seg) <= 255
        res = []
        n = len(s)
        for i in range(1, min(4, n-2)):
            for j in range(i+1, min(i+4, n-1)):
                for k in range(j+1, min(j+4, n)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if all(map(valid, [a,b,c,d])):
                        res.append(".".join([a,b,c,d]))
        return res
    
