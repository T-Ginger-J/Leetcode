// LeetCode 213: House Robber II
// Explanation:
// 1. Compute two linear rob cases — excluding first house and excluding last.
// 2. Return max of both.
// Time Complexity: O(n)
// Space Complexity: O(1)

#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        return max(robLine(nums, 0, nums.size()-2), robLine(nums, 1, nums.size()-1));
    }

private:
    int robLine(vector<int>& nums, int start, int end) {
        int prev = 0, curr = 0;
        for (int i = start; i <= end; ++i) {
            int temp = curr;
            curr = max(curr, prev + nums[i]);
            prev = temp;
        }
        return curr;
    }
};

// vector<int> nums = {2,3,2};
// Solution sol;
// cout << sol.rob(nums); // 3
//
// vector<int> nums2 = {1,2,3,1};
// cout << sol.rob(nums2); // 4
