# LeetCode 457: Circular Array Loop
# Explanation:
# Given a circular array nums, determine if there exists a cycle:
# - Cycle length > 1
# - All steps in the cycle move in the same direction (all positive or all negative)
#
# Method 1: Fast & Slow Pointers (Floyd’s Cycle Detection)
# - For each index, treat nums[i] as a jump length.
# - Use slow and fast pointers to detect cycles.
# - Invalidate visited paths that do not form valid cycles.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, next_index(i)
            direction = nums[i] > 0

            while (
                nums[fast] != 0 and
                nums[next_index(fast)] != 0 and
                (nums[fast] > 0) == direction and
                (nums[next_index(fast)] > 0) == direction
            ):
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # Mark visited nodes as invalid
            j = i
            while nums[j] != 0 and (nums[j] > 0) == direction:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt

        return False


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Valid positive cycle
print(sol.circularArrayLoop([2, -1, 1, 2, 2]))
# Expected output: True

# Example 2: Direction conflict
print(sol.circularArrayLoop([-1, 2]))
# Expected output: False

# Example 3: Self-loop only (invalid)
print(sol.circularArrayLoop([1, -1, 1, -1]))
# Expected output: False
