class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode(0);
    let current = dummy;
    let carry = 0;

    while (l1 !== null || l2 !== null || carry > 0) {
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;

        const sum = val1 + val2 + carry;
        carry = Math.floor(sum / 10);

        current.next = new ListNode(sum % 10);
        current = current.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }

    return dummy.next;
};

function addTwoNumbersRecursive(
    l1: ListNode | null,
    l2: ListNode | null,
    carry: number = 0
): ListNode | null {
    if (!l1 && !l2 && carry === 0) {
        return null; // base case: nothing left to add
    }

    const val1 = l1 ? l1.val : 0;
    const val2 = l2 ? l2.val : 0;
    const sum = val1 + val2 + carry;

    const newNode = new ListNode(sum % 10);
    newNode.next = addTwoNumbersRecursive(
        l1 ? l1.next : null,
        l2 ? l2.next : null,
        Math.floor(sum / 10)
    );

    return newNode;
}