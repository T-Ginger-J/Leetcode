// LeetCode 89: Gray Code
// Explanation:
// 1. Gray code formula: i ^ (i >> 1).
// 2. Generate sequence from 0 to (2^n - 1).
// Time Complexity: O(2^n)
// Space Complexity: O(2^n)

import java.util.*;

class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> res = new ArrayList<>();
        int size = 1 << n;
        for (int i = 0; i < size; i++) {
            res.add(i ^ (i >> 1));
        }
        return res;
    }
}
