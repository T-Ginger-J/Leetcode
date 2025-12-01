// LeetCode 318: Maximum Product of Word Lengths
// Explanation:
// Convert each word into a bitmask of letters.
// Check all pairs where (mask1 & mask2) === 0.
//
// Time Complexity: O(n^2)
// Space Complexity: O(n)

var maxProduct = function(words) {
    const n = words.length;
    const masks = new Array(n).fill(0);

    for (let i = 0; i < n; i++) {
        let mask = 0;
        for (const ch of new Set(words[i])) {
            mask |= 1 << (ch.charCodeAt(0) - 97);
        }
        masks[i] = mask;
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            if ((masks[i] & masks[j]) === 0) {
                ans = Math.max(ans, words[i].length * words[j].length);
            }
        }
    }
    return ans;
};
