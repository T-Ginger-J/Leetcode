// LeetCode 59: Spiral Matrix II
// Explanation:
// 1. Track four boundaries (top,bottom,left,right) and fill numbers while spiraling inward.
// Time Complexity: O(n^2)

var generateMatrix = function(n) {
    const matrix = Array.from({length: n}, () => Array(n).fill(0));
    let top = 0, bottom = n-1, left = 0, right = n-1;
    let num = 1;
    
    while (left <= right && top <= bottom) {
        for (let i = left; i <= right; i++) matrix[top][i] = num++;
        top++;
        for (let i = top; i <= bottom; i++) matrix[i][right] = num++;
        right--;
        if (top <= bottom) {
            for (let i = right; i >= left; i--) matrix[bottom][i] = num++;
            bottom--;
        }
        if (left <= right) {
            for (let i = bottom; i >= top; i--) matrix[i][left] = num++;
            left++;
        }
    }
    return matrix;
};

