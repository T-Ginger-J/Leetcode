class Solution:
    def countSmaller(self, nums):
        offset = abs(min(nums)) + 1  # shift negatives
        size = max(nums) + offset + 1
        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        res = []
        for num in reversed(nums):
            res.append(query(num + offset - 1))
            update(num + offset)
        return res[::-1]

