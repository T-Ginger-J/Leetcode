// LeetCode 141: Linked List Cycle
// Explanation:
// 1. Use Floyd’s Cycle Detection (Tortoise and Hare).
// 2. If fast and slow pointers meet, cycle exists.
// 3. If fast reaches null, no cycle.
// Time Complexity: O(n)
// Space Complexity: O(1)

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) return true;
        }
        return false;
    }
};
