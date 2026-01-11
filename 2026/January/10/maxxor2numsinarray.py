class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            prefixes = set(num & mask for num in nums)
            temp = max_xor | (1 << i)
            for p in prefixes:
                if temp ^ p in prefixes:
                    max_xor = temp
                    break
        return max_xor
