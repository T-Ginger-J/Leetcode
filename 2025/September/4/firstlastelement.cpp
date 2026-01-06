#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int first = findBound(nums, target, true);
        if (first == -1) return {-1, -1};
        int last = findBound(nums, target, false);
        return {first, last};
    }

private:
    int findBound(vector<int>& nums, int target, bool isFirst) {
        int left = 0, right = nums.size() - 1;
        int bound = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                bound = mid;
                if (isFirst) {
                    right = mid - 1;  // search left half
                } else {
                    left = mid + 1;   // search right half
                }
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return bound;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {5,7,7,8,8,10};
    vector<int> res = sol.searchRange(nums, 8);
    cout << "[" << res[0] << ", " << res[1] << "]\n"; // Output: [3, 4]

    res = sol.searchRange(nums, 6);
    cout << "[" << res[0] << ", " << res[1] << "]\n"; // Output: [-1, -1]
}
