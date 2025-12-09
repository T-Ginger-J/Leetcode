class Solution:
    def intersect(self, nums1, nums2):
        from collections import Counter
        count1 = Counter(nums1)
        res = []
        for num in nums2:
            if count1.get(num, 0) > 0:
                res.append(num)
                count1[num] -= 1
        return res
