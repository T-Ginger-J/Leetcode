// LeetCode 118: Pascal’s Triangle
// Explanation:
// 1. Each row starts and ends with 1.
// 2. Each middle element = sum of two elements above it.
// Time Complexity: O(n^2)
// Space Complexity: O(n^2)

#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle(numRows);
        for (int i = 0; i < numRows; ++i) {
            triangle[i].resize(i + 1, 1);
            for (int j = 1; j < i; ++j)
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
        return triangle;
    }
};

