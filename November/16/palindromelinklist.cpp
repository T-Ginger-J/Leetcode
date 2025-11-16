// LeetCode 234: Palindrome Linked List
// Explanation:
// 1. Find middle with fast/slow pointers.
// 2. Reverse second half.
// 3. Compare halves.
//
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    bool isPalindrome(ListNode* head) {
        if (!head || !head->next) return true;

        ListNode *slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse second half
        ListNode* prev = nullptr;
        while (slow) {
            ListNode* nxt = slow->next;
            slow->next = prev;
            prev = slow;
            slow = nxt;
        }

        // Compare
        ListNode* left = head;
        ListNode* right = prev;
        while (right) {
            if (left->val != right->val)
                return false;
            left = left->next;
            right = right->next;
        }
        return true;
    }
};
