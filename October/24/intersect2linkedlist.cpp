// LeetCode 160: Intersection of Two Linked Lists
// Explanation:
// 1. Use two pointers moving through both lists.
// 2. When one reaches the end, redirect to the other’s head.
// 3. They will meet at intersection or both end at null.
// Time Complexity: O(m + n)
// Space Complexity: O(1)

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (!headA || !headB) return nullptr;
        ListNode *a = headA, *b = headB;
        while (a != b) {
            a = a ? a->next : headB;
            b = b ? b->next : headA;
        }
        return a;
    }
};

#include <iostream>
using namespace std;

