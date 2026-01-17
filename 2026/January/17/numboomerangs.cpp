// LeetCode 447: Number of Boomerangs
// Explanation:
// Same problem description as the Python version above.
//
// Method 1: Hashmap Counting (Optimal, same logic)
// - For each point, count distances to other points.
// - For each distance with count c, add c*(c-1) boomerangs.
// Time Complexity: O(n^2), Space Complexity: O(n)

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int res = 0;
        for (auto& i : points) {
            unordered_map<int, int> dist_count;
            for (auto& j : points) {
                if (i == j) continue;
                int dx = i[0] - j[0];
                int dy = i[1] - j[1];
                int dist = dx*dx + dy*dy;
                dist_count[dist]++;
            }
            for (auto& [_, count] : dist_count) {
                res += count * (count - 1);
            }
        }
        return res;
    }
};

int main() {
    Solution sol;

    // Example 1: Simple line
    vector<vector<int>> points1 = {{0,0},{1,0},{2,0}};
    cout << sol.numberOfBoomerangs(points1) << endl;  
    // Expected output: 2

    // Example 2: Square points
    vector<vector<int>> points2 = {{0,0},{1,0},{0,1},{1,1}};
    cout << sol.numberOfBoomerangs(points2) << endl;  
    // Expected output: 8

    // Example 3: Single point
    vector<vector<int>> points3 = {{0,0}};
    cout << sol.numberOfBoomerangs(points3) << endl;  
    // Expected output: 0

    return 0;
}
