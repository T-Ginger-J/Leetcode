// LeetCode 148: Sort List
// Explanation:
// 1. Use merge sort (divide and conquer).
// 2. Find middle using fast/slow pointers.
// 3. Recursively sort left and right halves.
// 4. Merge sorted halves.
// Time Complexity: O(n log n)
// Space Complexity: O(log n)

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        slow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0), curr = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                curr.next = l1;
                l1 = l1.next;
            } else {
                curr.next = l2;
                l2 = l2.next;
            }
            curr = curr.next;
        }
        curr.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}

public class Main {
    static ListNode createList(int[] arr) {
        ListNode dummy = new ListNode(0), curr = dummy;
        for (int val : arr) {
            curr.next = new ListNode(val);
            curr = curr.next;
        }
        return dummy.next;
    }

    static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        ListNode head1 = createList(new int[]{4,2,1,3});
        printList(sol.sortList(head1)); // Output: 1 2 3 4

        ListNode head2 = createList(new int[]{-1,5,3,4,0});
        printList(sol.sortList(head2)); // Output: -1 0 3 4 5
    }
}
