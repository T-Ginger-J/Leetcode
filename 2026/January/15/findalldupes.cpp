// LeetCode 442: Find All Duplicates in an Array
// Explanation:
// Given an array nums of n integers where 1 ≤ nums[i] ≤ n, some elements appear twice and others appear once.
// The task is to find all elements that appear twice without using extra space (O(1) extra space allowed besides the output).
//
// Method 1: In-Place Negative Marking (Optimal)
// - Iterate through the array.
// - For each number nums[i], map it to index abs(nums[i]) - 1.
// - Negate the number at that index to mark it as seen.
// - If the number at that index is already negative, it is a duplicate.
//
// Time Complexity: O(n)
// Space Complexity: O(1) (ignoring output list)
//
// Method 2: Sorting (Not optimal for O(1) space)
// - Sort the array and compare neighbors to find duplicates.
// - Time: O(n log n), Space: O(1) if in-place sort allowed.

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    // Method 1: In-Place Negative Marking
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            if (nums[index] < 0)
                res.push_back(abs(nums[i]));
            else
                nums[index] = -nums[index];
        }
        return res;
    }
};
