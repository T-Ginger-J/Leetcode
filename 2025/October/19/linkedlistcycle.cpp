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

#include <iostream>
int main() {
    ListNode* n1 = new ListNode(3);
    ListNode* n2 = new ListNode(2);
    ListNode* n3 = new ListNode(0);
    ListNode* n4 = new ListNode(-4);
    n1->next = n2; n2->next = n3; n3->next = n4; n4->next = n2; // Cycle
    Solution s;
    std::cout << s.hasCycle(n1) << std::endl; // Output: 1 (True)

    ListNode* a = new ListNode(1);
    ListNode* b = new ListNode(2);
    a->next = b; // No cycle
    std::cout << s.hasCycle(a) << std::endl; // Output: 0 (False)
}
