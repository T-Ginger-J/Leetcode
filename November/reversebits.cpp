// LeetCode 190: Reverse Bits
// Explanation:
// 1. Iterate through all 32 bits.
// 2. Shift result left and add least significant bit of n.
// 3. Shift n right by one and continue.
// Time Complexity: O(1)
// Space Complexity: O(1)

#include <cstdint>
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        for (int i = 0; i < 32; i++) {
            result = (result << 1) | (n & 1);
            n >>= 1;
        }
        return result;
    }
};

#include <iostream>

int main() {
    Solution sol;
    cout << sol.reverseBits(0b00000010100101000001111010011100) << endl; // 964176192
    cout << sol.reverseBits(0b11111111111111111111111111111101) << endl; // 3221225471
    cout << sol.reverseBits(0) << endl;                                   // 0
    return 0;
}
