// LeetCode 215: Kth Largest Element in an Array
// Explanation:
// 1. Use std::priority_queue (min heap via greater comparator).
// 2. Keep heap size at most k, smallest in heap is kth largest.
// Time Complexity: O(n log k)
// Space Complexity: O(k)

#include <vector>
#include <queue>
#include <functional>
using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minHeap;
        for (int n : nums) {
            minHeap.push(n);
            if (minHeap.size() > k)
                minHeap.pop();
        }
        return minHeap.top();
    }
};

// vector<int> nums1 = {3,2,1,5,6,4};
// Solution sol;
// cout << sol.findKthLargest(nums1, 2); // 5
//
// vector<int> nums2 = {3,2,3,1,2,4,5,5,6};
// cout << sol.findKthLargest(nums2, 4); // 4
