// O(n)

package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy

    for head != nil && head.Next != nil {
        first := head
        second := head.Next

        // Swap
        prev.Next = second
        first.Next = second.Next
        second.Next = first

        // Move pointers
        prev = first
        head = first.Next
    }

    return dummy.Next
}

func swapPairsRecursive(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    first := head
    second := head.Next

    // Recursively swap the rest
    first.Next = swapPairs(second.Next)
    second.Next = first

    return second
}

// Helper functions for testing
func buildList(arr []int) *ListNode {
    dummy := &ListNode{}
    curr := dummy
    for _, v := range arr {
        curr.Next = &ListNode{Val: v}
        curr = curr.Next
    }
    return dummy.Next
}

func printList(node *ListNode) {
    for node != nil {
        fmt.Print(node.Val, " ")
        node = node.Next
    }
    fmt.Println()
}

func main() {
    head := buildList([]int{1, 2, 3, 4})
    swapped := swapPairs(head)
    printList(swapped) // Output: 2 1 4 3
}
