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

