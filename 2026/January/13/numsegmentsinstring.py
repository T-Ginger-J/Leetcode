# LeetCode 434: Number of Segments in a String
# Explanation:
# 1. A segment is defined as a contiguous sequence of non-space characters.
# 2. Split the string by spaces and count non-empty strings.
# 3. Alternatively, iterate through the string and count transitions from space to non-space.

class Solution:
    def countSegments(self, s: str) -> int:
        # Split by spaces and filter out empty strings
        return len([seg for seg in s.split(' ') if seg])

    def countSegmentsIterative(self, s: str) -> int:
        count = 0
        in_segment = False
        for char in s:
            if char != ' ' and not in_segment:
                count += 1
                in_segment = True
            elif char == ' ':
                in_segment = False
        return count
    
# Example 1
s = "Hello, my name is John"
# Output: 5
print(Solution().countSegments(s))

# Example 2
s = "   Hello   world  "
# Output: 2
print(Solution().countSegments(s))

# Example 3
s = ""
# Output: 0
print(Solution().countSegments(s))
 
