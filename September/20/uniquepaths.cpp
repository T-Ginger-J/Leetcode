// LeetCode 62: Unique Paths
// Explanation:
// 1. Use combinatorics: (m+n-2 choose m-1)
// 2. Compute result iteratively to avoid overflow
// Time Complexity: O(min(m,n))
// Space Complexity: O(1)

class Solution {
public:
    int uniquePaths(int m, int n) {
        long long res = 1;
        int k = min(m-1, n-1);
        int total = m+n-2;
        for (int i = 1; i <= k; i++) {
            res = res * (total - k + i) / i;
        }
        return (int)res;
    }
};

// Example usage:
// Solution sol;
// cout << sol.uniquePaths(3, 7) << endl; // 28
// cout << sol.uniquePaths(3, 2) << endl; // 3
