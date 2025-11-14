// LeetCode 226: Invert Binary Tree
// Explanation:
// 1. Recursively swap left and right subtrees.
// 2. Return root after recursion.
// Time Complexity: O(n)
// Space Complexity: O(h)

// Definition for a binary tree node.
struct TreeNode {
int val;
TreeNode *left;
TreeNode *right;
TreeNode() : val(0), left(nullptr), right(nullptr) {}
TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr;
        swap(root->left, root->right);
        invertTree(root->left);
        invertTree(root->right);
        return root;
    }
};

// TreeNode* root = new TreeNode(4,
//     new TreeNode(2, new TreeNode(1), new TreeNode(3)),
//     new TreeNode(7, new TreeNode(6), new TreeNode(9)));
// Solution sol;
// TreeNode* newRoot = sol.invertTree(root);
// // newRoot now represents [4,7,2,9,6,3,1]
