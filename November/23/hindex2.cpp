// Explanation:
// 1. citations is sorted ascending.
// 2. We binary search for minimum index i where citations[i] >= n - i.
// 3. The h-index is n - i.
// Time Complexity: O(log n)
// Space Complexity: O(1)

class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int l = 0, r = n - 1;

        while (l <= r) {
            int m = (l + r) / 2;
            if (citations[m] >= n - m)
                r = m - 1;
            else
                l = m + 1;
        }
        return n - l;
    }
};

// Example usage:
// Solution sol;
// cout << sol.hIndex(vector<int>{0,1,3,5,6}); // 3
// cout << sol.hIndex(vector<int>{1,2,100});   // 2
// cout << sol.hIndex(vector<int>{0});         // 0
