#include <stdio.h>
#include <stdlib.h>

// Definition for singly-linked list
struct ListNode {
    int val;
    struct ListNode *next;
};

// Helper: create a new node
struct ListNode* newNode(int val) {
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));
    node->val = val;
    node->next = NULL;
    return node;
}

// Merge two sorted lists
struct ListNode* mergeTwoLists(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode dummy;
    struct ListNode* current = &dummy;
    dummy.next = NULL;

    while (l1 && l2) {
        if (l1->val < l2->val) {
            current->next = l1;
            l1 = l1->next;
        } else {
            current->next = l2;
            l2 = l2->next;
        }
        current = current->next;
    }

    current->next = l1 ? l1 : l2;
    return dummy.next;
}

// Helper: print linked list
void printList(struct ListNode* head) {
    while (head) {
        printf("%d ", head->val);
        head = head->next;
    }
    printf("\n");
}

// Example usage
int main() {
    struct ListNode* l1 = newNode(1);
    l1->next = newNode(2);
    l1->next->next = newNode(4);

    struct ListNode* l2 = newNode(1);
    l2->next = newNode(3);
    l2->next->next = newNode(4);

    struct ListNode* merged = mergeTwoLists(l1, l2);
    printList(merged); // Output: 1 1 2 3 4 4

    return 0;
}
