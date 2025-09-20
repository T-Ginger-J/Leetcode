package main

import (
    "container/heap"
    "fmt"
)

// Definition for singly-linked list.
type ListNode struct {
    Val  int
    Next *ListNode
}

// Priority Queue Implementation
type PriorityQueue []*ListNode

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].Val < pq[j].Val
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PriorityQueue) Push(x interface{}) {
    *pq = append(*pq, x.(*ListNode))
}
func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    x := old[n-1]
    *pq = old[:n-1]
    return x
}

func mergeKLists(lists []*ListNode) *ListNode {
    pq := &PriorityQueue{}
    heap.Init(pq)

    // Push the head of each list into the heap
    for _, l := range lists {
        if l != nil {
            heap.Push(pq, l)
        }
    }

    dummy := &ListNode{}
    curr := dummy

    for pq.Len() > 0 {
        node := heap.Pop(pq).(*ListNode)
        curr.Next = node
        curr = curr.Next
        if node.Next != nil {
            heap.Push(pq, node.Next)
        }
    }

    return dummy.Next
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
    lists := []*ListNode{
        buildList([]int{1, 4, 5}),
        buildList([]int{1, 3, 4}),
        buildList([]int{2, 6}),
    }
    merged := mergeKLists(lists)
    printList(merged) // Output: 1 1 2 3 4 4 5 6
}
