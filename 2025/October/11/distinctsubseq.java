// LeetCode 115: Distinct Subsequences
// Explanation:
// 1. dp[i][j] = number of ways s[0..i-1] can form t[0..j-1].
// 2. Base: dp[i][0] = 1, since empty t is subsequence of any prefix of s.
// 3. Transition:
//    - If s[i-1] == t[j-1], dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
//    - Else dp[i][j] = dp[i-1][j]
// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

class Solution {
    public int numDistinct(String s, String t) {
        int m = s.length(), n = t.length();
        long[][] dp = new long[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++)
            dp[i][0] = 1;
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j];
            }
        }
        return (int) dp[m][n];
    }
}

// System.out.println(new Solution().numDistinct("rabbbit", "rabbit"));
// Output: 3

// System.out.println(new Solution().numDistinct("babgbag", "bag"));
// Output: 5

