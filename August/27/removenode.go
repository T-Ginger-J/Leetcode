package main

import "fmt"

// Definition for singly-linked list
type ListNode struct {
    Val  int
    Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummy := &ListNode{0, head}
    slow, fast := dummy, dummy

    // Move fast ahead by n+1 steps
    for i := 0; i < n+1; i++ {
        fast = fast.Next
    }

    // Move slow and fast together
    for fast != nil {
        slow = slow.Next
        fast = fast.Next
    }

    // Remove nth node
    slow.Next = slow.Next.Next

    return dummy.Next
}

// Helper function to create linked list from slice
func makeList(nums []int) *ListNode {
    dummy := &ListNode{}
    curr := dummy
    for _, val := range nums {
        curr.Next = &ListNode{Val: val}
        curr = curr.Next
    }
    return dummy.Next
}

// Helper function to print linked list
func printList(head *ListNode) {
    for head != nil {
        fmt.Print(head.Val, " ")
        head = head.Next
    }
    fmt.Println()
}

func main() {
    head := makeList([]int{1, 2, 3, 4, 5})
    newHead := removeNthFromEnd(head, 2)
    printList(newHead) // Output: 1 2 3 5
}
