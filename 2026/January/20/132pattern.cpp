// LeetCode 456: 132 Pattern
// Method: Monotonic Stack (Right-to-Left)
// Time Complexity: O(n)
// Space Complexity: O(n)

#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> st;
        int second = INT_MIN;

        for (int i = nums.size() - 1; i >= 0; i--) {
            if (nums[i] < second) return true;
            while (!st.empty() && nums[i] > st.top()) {
                second = st.top();
                st.pop();
            }
            st.push(nums[i]);
        }
        return false;
    }
};

int main() {
    Solution sol;

    // Example 1: Simple 132 pattern
    vector<int> nums1 = {3,1,4,2};
    cout << sol.find132pattern(nums1) << endl;
    // Expected output: 1 (true)

    // Example 2: Strictly increasing
    vector<int> nums2 = {1,2,3,4};
    cout << sol.find132pattern(nums2) << endl;
    // Expected output: 0 (false)

    // Example 3: Pattern with negative numbers
    vector<int> nums3 = {-1,3,2,0};
    cout << sol.find132pattern(nums3) << endl;
    // Expected output: 1 (true)

    return 0;
}
