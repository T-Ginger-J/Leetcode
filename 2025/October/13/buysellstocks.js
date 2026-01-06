// LeetCode 121: Best Time to Buy and Sell Stock
// Explanation:
// 1. Track minimum price seen so far.
// 2. Update max profit as we go.
// Time Complexity: O(n)
// Space Complexity: O(1)

var maxProfit = function(prices) {
    let minPrice = Infinity;
    let maxProfit = 0;
    for (let price of prices) {
        minPrice = Math.min(minPrice, price);
        maxProfit = Math.max(maxProfit, price - minPrice);
    }
    return maxProfit;
};

console.log(maxProfit([7,1,5,3,6,4])); // Output: 5
console.log(maxProfit([7,6,4,3,1]));   // Output: 0
