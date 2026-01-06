// Explanation:
// 1. Use the arithmetic sum formula 0..n and subtract array sum to get missing number.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int sum = 0;
        for(int num : nums) sum += num;
        return n * (n + 1) / 2 - sum;
    }
}

// Example usage:
// new Solution().missingNumber(new int[]{3,0,1}); // 2
// new Solution().missingNumber(new int[]{0,1});   // 2
// new Solution().missingNumber(new int[]{9,6,4,2,3,5,7,0,1}); // 8
