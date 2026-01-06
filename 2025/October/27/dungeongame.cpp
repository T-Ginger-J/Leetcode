// LeetCode 174: Dungeon Game
// Explanation:
// 1. Dynamic programming from bottom-right to top-left.
// 2. dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
// 3. dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        int m = dungeon.size(), n = dungeon[0].size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MAX));
        dp[m][n - 1] = dp[m - 1][n] = 1;

        for (int i = m - 1; i >= 0; --i) {
            for (int j = n - 1; j >= 0; --j) {
                int need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
                dp[i][j] = max(1, need);
            }
        }
        return dp[0][0];
    }
};

int main() {
    Solution sol;
    vector<vector<int>> dungeon1 = {{-2,-3,3},{-5,-10,1},{10,30,-5}};
    vector<vector<int>> dungeon2 = {{0}};
    vector<vector<int>> dungeon3 = {{1,-2,3},{2,-2,-2}};

    cout << sol.calculateMinimumHP(dungeon1) << endl; // 7
    cout << sol.calculateMinimumHP(dungeon2) << endl; // 1
    cout << sol.calculateMinimumHP(dungeon3) << endl; // 2
}
