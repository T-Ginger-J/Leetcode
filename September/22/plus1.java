// LeetCode 66: Plus One
// Explanation:
// 1. Traverse from last digit backwards.
// 2. Handle carry if digit is 9.
// 3. If all 9's, return array with extra digit.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] res = new int[digits.length + 1];
        res[0] = 1;
        return res;
    }
}

// Example usage:
// Solution sol = new Solution();
// System.out.println(Arrays.toString(sol.plusOne(new int[]{1,2,3}))); // [1,2,4]
// System.out.println(Arrays.toString(sol.plusOne(new int[]{9})));     // [1,0]
