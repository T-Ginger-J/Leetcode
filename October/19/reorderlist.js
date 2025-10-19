// LeetCode 143: Reorder List
// Explanation:
// 1. Find middle using slow/fast pointers.
// 2. Reverse second half.
// 3. Merge halves alternatingly.
// Time Complexity: O(n)
// Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
var reorderList = function(head) {
    if (!head || !head.next) return;

    // Step 1: Find middle
    let slow = head, fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    // Step 2: Reverse second half
    let prev = null, curr = slow.next;
    slow.next = null;
    while (curr) {
        let nextTemp = curr.next;
        curr.next = prev;
        prev = curr;
        curr = nextTemp;
    }

    // Step 3: Merge two halves
    let first = head, second = prev;
    while (second) {
        let tmp1 = first.next, tmp2 = second.next;
        first.next = second;
        second.next = tmp1;
        first = tmp1;
        second = tmp2;
    }
};
