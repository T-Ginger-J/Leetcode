// LeetCode 92: Reverse Linked List II
// Explanation:
// 1. Use dummy node to handle head reversals.
// 2. Traverse to node before 'left'.
// 3. Reverse sublist using head-insertion method.
// 4. Reconnect reversed part back.
// Time Complexity: O(n)
// Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
var reverseBetween = function(head, left, right) {
    if (!head || left === right) return head;
    let dummy = new ListNode(0, head);
    let prev = dummy;

    // Move prev to node before 'left'
    for (let i = 0; i < left - 1; i++) {
        prev = prev.next;
    }

    let curr = prev.next;
    for (let i = 0; i < right - left; i++) {
        let temp = curr.next;
        curr.next = temp.next;
        temp.next = prev.next;
        prev.next = temp;
    }

    return dummy.next;
};

// Helper functions
function buildList(arr) {
    let dummy = new ListNode(0), curr = dummy;
    for (let v of arr) {
        curr.next = new ListNode(v);
        curr = curr.next;
    }
    return dummy.next;
}
function toArray(head) {
    let res = [];
    while (head) {
        res.push(head.val);
        head = head.next;
    }
    return res;
}

// Example 1
let head1 = buildList([1,2,3,4,5]);
let res1 = reverseBetween(head1, 2, 4);
console.log(toArray(res1)); // [1,4,3,2,5]

// Example 2
let head2 = buildList([5]);
let res2 = reverseBetween(head2, 1, 1);
console.log(toArray(res2)); // [5]
