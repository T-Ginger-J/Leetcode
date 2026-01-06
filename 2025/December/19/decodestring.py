# LeetCode 394: Decode String
# Explanation:
# 1. Use stack to track counts and current strings
# 2. Build decoded string iteratively
# Time Complexity: O(n * k_max)
# Space Complexity: O(n)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""
        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch
        return curr_str
    
print(Solution().decodeString("3[a]2[bc]"))       # Output: "aaabcbc"
print(Solution().decodeString("3[a2[c]]"))        # Output: "accaccacc"
print(Solution().decodeString("2[abc]3[cd]ef"))   # Output: "abcabccdcdcdef"

