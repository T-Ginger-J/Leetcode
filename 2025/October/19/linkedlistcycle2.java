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

public class Main {
    public static void main(String[] args) {
        ListNode n1 = new ListNode(3);
        ListNode n2 = new ListNode(2);
        ListNode n3 = new ListNode(0);
        ListNode n4 = new ListNode(-4);
        n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n2;

        Solution sol = new Solution();
        System.out.println(sol.detectCycle(n1).val); // Output: 2

        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        a.next = b;
        System.out.println(sol.detectCycle(a)); // Output: null
    }
}
