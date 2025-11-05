// LeetCode 200: Number of Islands
// Explanation:
// 1. Use DFS to traverse connected land components.
// 2. Mark visited cells as '0'.
// Time Complexity: O(m * n)
// Space Complexity: O(m * n)

#include <vector>
using namespace std;

class Solution {
public:
    void dfs(vector<vector<char>>& grid, int r, int c) {
        int rows = grid.size(), cols = grid[0].size();
        if (r < 0 || c < 0 || r >= rows || c >= cols || grid[r][c] == '0')
            return;
        grid[r][c] = '0';
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }

    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size(), cols = grid[0].size(), count = 0;
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] == '1') {
                    count++;
                    dfs(grid, r, c);
                }
            }
        }
        return count;
    }
};

// Input:
// [
//  ['1','1','0','0','0'],
//  ['1','1','0','0','0'],
//  ['0','0','1','0','0'],
//  ['0','0','0','1','1']
// ]
// Output: 3
