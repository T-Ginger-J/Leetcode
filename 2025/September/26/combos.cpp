// LeetCode 77: Combinations
// Explanation:
// 1. Use backtracking to generate all valid combinations.
// 2. Stop when current combination has size k.
// Time Complexity: O(C(n, k) * k)
// Space Complexity: O(k)

class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> comb;
        backtrack(1, n, k, comb, res);
        return res;
    }

    void backtrack(int start, int n, int k, vector<int>& comb, vector<vector<int>>& res) {
        if (comb.size() == k) {
            res.push_back(comb);
            return;
        }
        for (int i = start; i <= n; i++) {
            comb.push_back(i);
            backtrack(i + 1, n, k, comb, res);
            comb.pop_back();
        }
    }
};

// Example usage:
// Solution sol;
// auto ans = sol.combine(4, 2);
// for (auto& v : ans) {
//     for (int x : v) cout << x << " ";
//     cout << endl;
// }
// // [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
