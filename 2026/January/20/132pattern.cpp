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

