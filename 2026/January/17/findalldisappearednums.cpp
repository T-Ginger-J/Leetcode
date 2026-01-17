#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++) {
            int index = abs(nums[i]) - 1;
            nums[index] = -abs(nums[index]);
        }
        vector<int> res;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) res.push_back(i + 1);
        }
        return res;
    }
};

int main() {
    Solution sol;

    // Example 1: Missing multiple numbers
    vector<int> nums1 = {4,3,2,7,8,2,3,1};
    vector<int> res1 = sol.findDisappearedNumbers(nums1);
    for (int x : res1) cout << x << " ";
    cout << endl;
    // Expected output: 5 6

    // Example 2: No missing numbers
    vector<int> nums2 = {1,2,3,4,5};
    vector<int> res2 = sol.findDisappearedNumbers(nums2);
    for (int x : res2) cout << x << " ";
    cout << endl;
    // Expected output: (empty)

    // Example 3: All numbers missing except one
    vector<int> nums3 = {2,2,2,2};
    vector<int> res3 = sol.findDisappearedNumbers(nums3);
    for (int x : res3) cout << x << " ";
    cout << endl;
    // Expected output: 1 3 4

    return 0;
}
