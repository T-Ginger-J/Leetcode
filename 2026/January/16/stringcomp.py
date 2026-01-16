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
