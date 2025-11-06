// LeetCode 199: Binary Tree Right Side View
// Explanation:
// 1. Use level-order traversal (BFS).
// 2. Record the last element at each level.
// Time Complexity: O(n)
// Space Complexity: O(n)

#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (!root) return result;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode* node = q.front(); q.pop();
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
                if (i == size - 1)
                    result.push_back(node->val);
            }
        }
        return result;
    }
};

// Example tree: [1,2,3,null,5,null,4]
// Output: [1,3,4]
