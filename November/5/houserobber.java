// LeetCode 198: House Robber
// Explanation:
// 1. Use dynamic programming with rolling variables.
// 2. At each house, choose between robbing or skipping.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int rob(int[] nums) {
        int prev1 = 0, prev2 = 0;
        for (int n : nums) {
            int temp = prev1;
            prev1 = Math.max(prev1, prev2 + n);
            prev2 = temp;
        }
        return prev1;
    }
}

/*
Solution sol = new Solution();
System.out.println(sol.rob(new int[]{1,2,3,1}));   // 4
System.out.println(sol.rob(new int[]{2,7,9,3,1})); // 12

 */