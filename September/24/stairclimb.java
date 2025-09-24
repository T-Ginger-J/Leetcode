// LeetCode 70: Climbing Stairs
// Explanation:
// 1. Equivalent to Fibonacci sequence.
// 2. Use iteration with two variables.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}

// Example usage:
// Solution sol = new Solution();
// System.out.println(sol.climbStairs(2)); // 2
// System.out.println(sol.climbStairs(3)); // 3
