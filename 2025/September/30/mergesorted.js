// LeetCode 88: Merge Sorted Array
// Explanation:
// 1. Use three pointers: i for nums1's valid part, j for nums2, k for end of nums1.
// 2. Start from the back, compare nums1[i] and nums2[j].
// 3. Place the larger element at nums1[k], move pointers.
// 4. Copy remaining nums2 elements if any.
// Time Complexity: O(m + n)
// Space Complexity: O(1)

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let i = m - 1, j = n - 1, k = m + n - 1;
    while (i >= 0 && j >= 0) {
        if (nums1[i] > nums2[j]) {
            nums1[k--] = nums1[i--];
        } else {
            nums1[k--] = nums2[j--];
        }
    }
    while (j >= 0) {
        nums1[k--] = nums2[j--];
    }
};

// Example 1
let nums1 = [1,2,3,0,0,0], m = 3;
let nums2 = [2,5,6], n = 3;
merge(nums1, m, nums2, n);
console.log(nums1); // [1,2,2,3,5,6]

// Example 2
nums1 = [4,5,6,0,0,0]; m = 3;
nums2 = [1,2,3]; n = 3;
merge(nums1, m, nums2, n);
console.log(nums1); // [1,2,3,4,5,6]
