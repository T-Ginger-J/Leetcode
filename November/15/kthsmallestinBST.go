// LeetCode 230: Kth Smallest Element in a BST
// Explanation:
// Inorder traversal yields nodes in sorted order.
// Count nodes until the k-th is reached.
//
// Time Complexity: O(h + k)
// Space Complexity: O(h)

package main

type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

func kthSmallest(root *TreeNode, k int) int {
    stack := []*TreeNode{}
    curr := root

    for {
        for curr != nil {
            stack = append(stack, curr)
            curr = curr.Left
        }
        curr = stack[len(stack)-1]
        stack = stack[:len(stack)-1]

        k--
        if k == 0 {
            return curr.Val
        }

        curr = curr.Right
    }
}

