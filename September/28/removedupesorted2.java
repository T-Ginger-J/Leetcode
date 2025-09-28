// LeetCode 82: Remove Duplicates from Sorted List II
// Explanation:
// 1. Use dummy node to simplify head removal.
// 2. Skip all nodes with duplicate values.
// 3. Connect previous pointer to next distinct node.
// Time Complexity: O(n)
// Space Complexity: O(1)

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val) {
                    head = head.next;
                }
                prev.next = head.next;
            } else {
                prev = prev.next;
            }
            head = head.next;
        }
        return dummy.next;
    }
}

// Example usage:
// public static void main(String[] args) {
//     Solution sol = new Solution();
//     ListNode head = new ListNode(1, new ListNode(2, new ListNode(3,
//                     new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5)))))));
//     ListNode result = sol.deleteDuplicates(head);
//     while (result != null) {
//         System.out.print(result.val + " "); // 1 2 5
//         result = result.next;
//     }
// }
