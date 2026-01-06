# LeetCode 318: Maximum Product of Word Lengths
# Explanation:
# Problem:
#   Find two words without common letters whose lengths' product is maximum.
#
# Approach (Bitmasking):
# 1. Convert each word into a 26-bit integer mask.
#    - If word contains 'a', set bit 0
#    - If contains 'b', set bit 1
#    ...
#    - If contains 'z', set bit 25
# 2. Two words share NO common letters ⇔ (mask1 & mask2) == 0
# 3. Check all word pairs and track max product.
#
# Time Complexity:  O(n^2)
# Space Complexity: O(n)

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

print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])) 
# Output: 16  ("abcw" * "xtfn")

print(Solution().maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))    
# Output: 4   ("ab" * "cd")

print(Solution().maxProduct(["a","aa","aaa","aaaa"]))                  
# Output: 0   (all share 'a')

