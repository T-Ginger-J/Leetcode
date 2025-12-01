class Solution:
    def maxProduct(self, words):
        n = len(words)
        masks = [0] * n
        
        for i, w in enumerate(words):
            mask = 0
            for ch in set(w):
                mask |= 1 << (ord(ch) - 97)
            masks[i] = mask
        
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans
