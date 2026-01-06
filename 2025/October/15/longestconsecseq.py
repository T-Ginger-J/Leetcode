# LeetCode 128: Longest Consecutive Sequence
# Explanation:
# 1. Use a set for O(1) lookups.
# 2. For each number, check if it’s the start of a sequence (num - 1 not in set).
# 3. Count the consecutive numbers and update the max length.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest


    def longestConsecutiveOneLine(self, A):
        S=set(A)
        return max(((lambda x:sum(1 for _ in iter(int,1) if x+(_:=0)in S and not S.discard(x+_)))(x) for x in S if x-1 not in S), default=0)
    
print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
# Output: 4  (sequence: 1, 2, 3, 4)

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
# Output: 9  (sequence: 0,1,2,3,4,5,6,7,8)

print(Solution().longestConsecutive([]))
# Output: 0
