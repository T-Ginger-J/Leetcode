#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0], curr = 0;
        for (int n : nums) {
            curr = max(n, curr + n);   // choose to start new subarray or extend
            maxSum = max(maxSum, curr);
        }
        return maxSum;
    }
};
