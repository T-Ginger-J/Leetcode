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

