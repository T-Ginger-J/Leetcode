// LeetCode 95: Unique Binary Search Trees II
// Explanation:
// 1. Use recursion to generate all possible BSTs for range [start, end].
// 2. For each i in range, build all combinations of left and right subtrees.
// 3. Use memoization (optional) for efficiency.
// Time Complexity: O(Cn)
// Space Complexity: O(Cn)

#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return build(1, n);
    }

private:
    vector<TreeNode*> build(int start, int end) {
        vector<TreeNode*> res;
        if (start > end) {
            res.push_back(nullptr);
            return res;
        }

        for (int i = start; i <= end; ++i) {
            vector<TreeNode*> left = build(start, i - 1);
            vector<TreeNode*> right = build(i + 1, end);
            for (auto l : left) {
                for (auto r : right) {
                    TreeNode* root = new TreeNode(i);
                    root->left = l;
                    root->right = r;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
};

