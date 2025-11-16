// LeetCode 233: Number of Digit One
// Explanation:
// Count '1's for each positional factor.
// Time Complexity: O(log n)
// Space Complexity: O(1)

var countDigitOne = function(n) {
    let factor = 1;
    let count = 0;

    while (factor <= n) {
        const left = Math.floor(n / (factor * 10));
        const digit = Math.floor(n / factor) % 10;
        const right = n % factor;

        if (digit === 0) count += left * factor;
        else if (digit === 1) count += left * factor + right + 1;
        else count += (left + 1) * factor;

        factor *= 10;
    }

    return count;
};

