// LeetCode 90: Subsets II
// Explanation:
// 1. Sort nums to handle duplicates.
// 2. Use backtracking, skipping duplicates (nums[i] == nums[i-1]).
// 3. Generate all unique subsets.
// Time Complexity: O(2^n)
// Space Complexity: O(2^n)

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> path;
        sort(nums.begin(), nums.end());
        backtrack(nums, 0, path, res);
        return res;
    }
    
    void backtrack(vector<int>& nums, int start, vector<int>& path, vector<vector<int>>& res) {
        res.push_back(path);
        for (int i = start; i < nums.size(); i++) {
            if (i > start && nums[i] == nums[i-1]) continue;
            path.push_back(nums[i]);
            backtrack(nums, i+1, path, res);
            path.pop_back();
        }
    }
};

// Example 1
Solution sol;
vector<int> nums1 = {1,2,2};
auto res1 = sol.subsetsWithDup(nums1);
// res1 = [[], [1], [2], [1,2], [2,2], [1,2,2]]

// Example 2
vector<int> nums2 = {0};
auto res2 = sol.subsetsWithDup(nums2);
// res2 = [[], [0]]