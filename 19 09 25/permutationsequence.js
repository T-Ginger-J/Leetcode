// LeetCode 60: Permutation Sequence
// Explanation:
// 1. Use factorial blocks to find which number to choose at each step
// 2. Remove chosen numbers from the list as we build the result
// Time Complexity: O(n^2)
// Space Complexity: O(n)

var getPermutation = function(n, k) {
    const fact = [1];
    for (let i = 1; i <= n; i++) fact[i] = fact[i-1]*i;
    const nums = [];
    for (let i = 1; i <= n; i++) nums.push(i.toString());
    k--;
    let res = '';
    for (let i = n; i >= 1; i--) {
        const idx = Math.floor(k / fact[i-1]);
        res += nums[idx];
        nums.splice(idx, 1);
        k %= fact[i-1];
    }
    return res;
};

