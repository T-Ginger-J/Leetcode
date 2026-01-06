// LeetCode 96: Unique Binary Search Trees
// Explanation:
// 1. Use DP: dp[i] = Σ dp[j-1] * dp[i-j] for j in [1..i]
// 2. Each j represents root, dividing into left/right subtrees.
// 3. Base: dp[0] = dp[1] = 1
// Time Complexity: O(n^2)
// Space Complexity: O(n)

class Solution {
    public int numTrees(int n) {
        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        return dp[n];
    }
}

Solution sol = new Solution();
System.out.println(sol.numTrees(3)); // 5
System.out.println(sol.numTrees(1)); // 1
System.out.println(sol.numTrees(5)); // 42
