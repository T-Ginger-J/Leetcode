// LeetCode 188: Best Time to Buy and Sell Stock IV
// Explanation:
// 1. If k >= n/2, treat as infinite transactions.
// 2. Otherwise use DP:
//    dp[i][j] = max profit using i transactions up to day j.
//    Use a rolling best_buy to optimize transitions.
// Time Complexity: O(k * n)
// Space Complexity: O(k * n)

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n < 2) return 0;
        if (k >= n / 2) {
            int profit = 0;
            for (int i = 1; i < n; i++)
                profit += max(0, prices[i] - prices[i-1]);
            return profit;
        }

        vector<vector<int>> dp(k + 1, vector<int>(n, 0));
        for (int i = 1; i <= k; i++) {
            int bestBuy = -prices[0];
            for (int j = 1; j < n; j++) {
                dp[i][j] = max(dp[i][j-1], prices[j] + bestBuy);
                bestBuy = max(bestBuy, dp[i-1][j-1] - prices[j]);
            }
        }
        return dp[k][n-1];
    }
};

#include <iostream>

int main() {
    Solution sol;
    cout << sol.maxProfit(2, vector<int>{2,4,1}) << endl;           // 2
    cout << sol.maxProfit(2, vector<int>{3,2,6,5,0,3}) << endl;     // 7
    cout << sol.maxProfit(3, vector<int>{1,2,4,2,5,7,2,4,9,0}) << endl; // 15
    return 0;
}
