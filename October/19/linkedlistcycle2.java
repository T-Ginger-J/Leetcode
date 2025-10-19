// LeetCode 142: Linked List Cycle II
// Explanation:
// 1. Detect cycle using Floyd’s Tortoise and Hare.
// 2. Once cycle detected, move one pointer to head.
// 3. Move both one step at a time until they meet — cycle start.
// Time Complexity: O(n)
// Space Complexity: O(1)

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next = null; }
}

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }
}
