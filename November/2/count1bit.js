// LeetCode 191: Number of 1 Bits
// Explanation:
// 1. Loop until n == 0.
// 2. Add n & 1 to count each time the lowest bit is 1.
// 3. Right shift n by one each iteration.
// Time Complexity: O(1) (32 iterations)
// Space Complexity: O(1)

var hammingWeight = function(n) {
    let count = 0;
    while (n !== 0) {
        count += n & 1;
        n >>>= 1; // unsigned right shift
    }
    return count;
};

console.log(hammingWeight(0b00000000000000000000000000001011)); // 3
console.log(hammingWeight(0b00000000000000000000000010000000)); // 1
console.log(hammingWeight(0b11111111111111111111111111111101)); // 31
