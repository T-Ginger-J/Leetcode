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

function ListNode(val, next) {
    this.val = val ?? 0;
    this.next = next ?? null;
}

function printList(head) {
    let res = [];
    while (head) { res.push(head.val); head = head.next; }
    console.log(res);
}

let head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));
reorderList(head);
printList(head); // ✅ [1, 4, 2, 3]

let head2 = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));
reorderList(head2);
printList(head2); // ✅ [1, 5, 2, 4, 3]

