// LeetCode 152: Maximum Product Subarray
// Explanation:
// 1. Track both current max and min products since negatives flip signs.
// 2. For each number, update max/min based on previous values.
// 3. Result is global maximum of all local maximums.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int maxProduct(int[] nums) {
        int res = nums[0];
        int curMax = nums[0], curMin = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int temp = curMax;
            curMax = Math.max(nums[i], Math.max(curMax * nums[i], curMin * nums[i]));
            curMin = Math.min(nums[i], Math.min(temp * nums[i], curMin * nums[i]));
            res = Math.max(res, curMax);
        }
        return res;
    }
}
