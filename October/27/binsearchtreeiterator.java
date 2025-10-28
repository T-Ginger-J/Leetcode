// LeetCode 173: Binary Search Tree Iterator
// Explanation:
// 1. Use a stack to simulate in-order traversal.
// 2. Push all left nodes initially.
// 3. On next(), pop top and push its right subtree’s left chain.
// Time Complexity: O(1) amortized
// Space Complexity: O(h)

class BSTIterator {
    private Stack<TreeNode> stack = new Stack<>();

    public BSTIterator(TreeNode root) {
        pushLeft(root);
    }

    private void pushLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }

    public int next() {
        TreeNode node = stack.pop();
        if (node.right != null) pushLeft(node.right);
        return node.val;
    }

    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/*
TreeNode root = new TreeNode(7, new TreeNode(3), new TreeNode(15, new TreeNode(9), new TreeNode(20)));
BSTIterator iterator = new BSTIterator(root);
System.out.println(iterator.next());     // 3
System.out.println(iterator.next());     // 7
System.out.println(iterator.hasNext());  // true
System.out.println(iterator.next());     // 9
System.out.println(iterator.next());     // 15
System.out.println(iterator.next());     // 20
System.out.println(iterator.hasNext());  // false
 */