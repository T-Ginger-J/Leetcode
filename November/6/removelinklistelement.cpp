// LeetCode 203: Remove Linked List Elements
// Explanation:
// 1. Use dummy node to handle head deletions easily.
// 2. Traverse and relink nodes skipping those with target val.
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* curr = &dummy;
        while (curr->next) {
            if (curr->next->val == val)
                curr->next = curr->next->next;
            else
                curr = curr->next;
        }
        return dummy.next;
    }
};
