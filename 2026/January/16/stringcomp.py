# LeetCode 443: String Compression
# Explanation:
# Given an array of characters chars, compress it in-place such that:
# - Consecutive repeating characters are replaced by the character followed by the count.
# - Single characters remain as is.
# Return the new length of the array after compression.
#
# Method 1: Two Pointers (Optimal)
# - Use read and write pointers:
#   1. Read through the array.
#   2. Count consecutive repeating characters.
#   3. Write the character to write pointer.
#   4. If count > 1, write the digits of the count individually.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (in-place)

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            char = chars[read]
            count = 0
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
                    
        return write

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple repeat
chars1 = ["a","a","b","b","c","c","c"]
length1 = sol.compress(chars1)
print(length1, chars1[:length1])  
# Expected output: 6, ["a","2","b","2","c","3"]

# Example 2: Single characters only
chars2 = ["a","b","c"]
length2 = sol.compress(chars2)
print(length2, chars2[:length2])  
# Expected output: 3, ["a","b","c"]

# Example 3: Long repeat count
chars3 = ["a"] * 12
length3 = sol.compress(chars3)
print(length3, chars3[:length3])  
# Expected output: 3, ["a","1","2"]
