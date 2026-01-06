// LeetCode 209: Minimum Size Subarray Sum
// Explanation:
// 1. Maintain a sliding window using two pointers.
// 2. Expand right until sum >= target, then shrink from left.
// 3. Track the smallest window length found.
// Time Complexity: O(n)
// Space Complexity: O(1)

var minSubArrayLen = function(target, nums) {
    let left = 0, sum = 0, minLen = Infinity;
    for (let right = 0; right < nums.length; right++) {
        sum += nums[right];
        while (sum >= target) {
            minLen = Math.min(minLen, right - left + 1);
            sum -= nums[left++];
        }
    }
    return minLen === Infinity ? 0 : minLen;
};

console.log(minSubArrayLen(7, [2,3,1,2,4,3])); // 2
console.log(minSubArrayLen(4, [1,4,4]));       // 1
console.log(minSubArrayLen(11, [1,1,1,1,1]));  // 0
