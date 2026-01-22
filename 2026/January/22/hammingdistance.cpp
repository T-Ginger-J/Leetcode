// LeetCode 461: Hamming Distance
// Method: XOR + Brian Kernighan’s Bit Counting
// Time Complexity: O(number of set bits)
// Space Complexity: O(1)

#include <iostream>
using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
        int n = x ^ y;
        int count = 0;
        while (n) {
            n &= (n - 1);
            count++;
        }
        return count;
    }
};

