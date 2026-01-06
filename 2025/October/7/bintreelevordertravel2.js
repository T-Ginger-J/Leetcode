// LeetCode 107: Binary Tree Level Order Traversal II
// Explanation:
// 1. Use BFS with a queue.
// 2. Add each level’s nodes to result.
// 3. Reverse result at the end for bottom-up order.
// Time Complexity: O(n)
// Space Complexity: O(n)

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
var levelOrderBottom = function(root) {
    if (!root) return [];
    let queue = [root], res = [];
    while (queue.length) {
        let level = [];
        let size = queue.length;
        for (let i = 0; i < size; i++) {
            let node = queue.shift();
            level.push(node.val);
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        res.unshift(level);
    }
    return res;
};

let root = { val: 3, left: { val: 9 }, right: { val: 20, left: { val: 15 }, right: { val: 7 } } };
console.log(levelOrderBottom(root)); // [[15,7],[9,20],[3]]

let root2 = { val: 1 };
console.log(levelOrderBottom(root2)); // [[1]]

console.log(levelOrderBottom(null)); // []
