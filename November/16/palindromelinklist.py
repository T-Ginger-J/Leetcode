# LeetCode 234: Palindrome Linked List
# Explanation:
# 1. Use fast/slow pointers to find the middle.
# 2. Reverse the second half of the list.
# 3. Compare the first half with the reversed second half.
# 4. (Optional) Restore the list.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

# Example usage:
# sol = Solution()
# print(sol.isPalindrome(ListNode.from_list([1,2,2,1]))) # True
# print(sol.isPalindrome(ListNode.from_list([1,2])))     # False
