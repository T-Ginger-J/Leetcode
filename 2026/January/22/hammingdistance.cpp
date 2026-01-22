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

int main() {
    Solution sol;

    // Example 1: Same numbers
    cout << sol.hammingDistance(5, 5) << endl;
    // Expected output: 0

    // Example 2: Completely different bits
    cout << sol.hammingDistance(0, 15) << endl;
    // Expected output: 4

    // Example 3: One-bit difference
    cout << sol.hammingDistance(1, 3) << endl;
    // Expected output: 1

    return 0;
}
