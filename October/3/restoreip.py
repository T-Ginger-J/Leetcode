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
