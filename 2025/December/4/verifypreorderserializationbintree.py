# LeetCode 331: Verify Preorder Serialization of a Binary Tree
# Explanation (Slot Counting):
# 1. A binary tree uses "slots" to place nodes.
# 2. Start with 1 slot for the root.
# 3. Every node consumes 1 slot.
#       - If it's a number (non-null), it creates 2 new slots.
#       - If it's '#', it creates 0 new slots.
# 4. If at any point slots < 0 → invalid.
# 5. At the end, valid serialization must end with exactly 0 slots.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1

        for node in nodes:
            slots -= 1
            if slots < 0:
                return False
            if node != '#':
                slots += 2

        return slots == 0

# Example 1
pre = "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: True
print(Solution().isValidSerialization(pre))

# Example 2
pre = "1,#"
# Output: False
print(Solution().isValidSerialization(pre))

# Example 3
pre = "9,#,#,1"
# Output: False
print(Solution().isValidSerialization(pre))
