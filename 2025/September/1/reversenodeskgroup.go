package main

import "fmt"

// Definition for singly-linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy

    for {
        // Find kth node from prev
        kth := prev
        for i := 0; i < k && kth != nil; i++ {
            kth = kth.Next
        }
        if kth == nil {
            break
        }

        groupNext := kth.Next

        // reverse the group
        prevCurr := groupNext
        curr := prev.Next

        for curr != groupNext {
            tmp := curr.Next
            curr.Next = prevCurr
            prevCurr = curr
            curr = tmp
        }

        tmp := prev.Next
        prev.Next = kth
        prev = tmp
    }

    return dummy.Next
}



// Helper functions
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
    head := buildList([]int{1, 2, 3, 4, 5})
    res := reverseKGroup(head, 2)
    printList(res) // Output: 2 1 4 3 5

    head2 := buildList([]int{1, 2, 3, 4, 5})
    res2 := reverseKGroup(head2, 3)
    printList(res2) // Output: 3 2 1 4 5
}
