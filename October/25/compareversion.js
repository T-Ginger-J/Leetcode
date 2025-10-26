// LeetCode 165: Compare Version Numbers
// Explanation:
// 1. Split both version strings by '.' and compare part by part.
// 2. Treat missing parts as 0.
// 3. Return 1, -1, or 0 accordingly.
// Time Complexity: O(n)
// Space Complexity: O(n)

var compareVersion = function(version1, version2) {
    const v1 = version1.split('.').map(Number);
    const v2 = version2.split('.').map(Number);
    const n = Math.max(v1.length, v2.length);
    for (let i = 0; i < n; i++) {
        const a = v1[i] || 0, b = v2[i] || 0;
        if (a > b) return 1;
        if (a < b) return -1;
    }
    return 0;
};

console.log(compareVersion("1.01", "1.001")); // Output: 0
console.log(compareVersion("1.0", "1.0.0"));  // Output: 0
console.log(compareVersion("0.1", "1.1"));    // Output: -1
