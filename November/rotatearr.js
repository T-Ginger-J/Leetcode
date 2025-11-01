// LeetCode 189: Rotate Array
// Explanation:
// 1. We can reverse the array in three steps (like Python version).
// 2. Helper reverse() swaps elements in-place.
// Time Complexity: O(n)
// Space Complexity: O(1)

var rotate = function(nums, k) {
    const n = nums.length;
    k = k % n;
    
    const reverse = (arr, start, end) => {
        while (start < end) {
            [arr[start], arr[end]] = [arr[end], arr[start]];
            start++; end--;
        }
    };
    
    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);
};

