// LeetCode 112: Path Sum
// Explanation:
// 1. DFS approach: subtract node value from targetSum at each step.
// 2. If we reach a leaf node and targetSum == node.val, return true.
// 3. Recurse left and right until path found or tree ends.
// Time Complexity: O(n)
// Space Complexity: O(h)

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null && targetSum == root.val)
            return true;
        targetSum -= root.val;
        return hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum);
    }
}
