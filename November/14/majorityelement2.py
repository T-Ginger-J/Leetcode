class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        threshold = len(nums) // 3
        return [x for x, c in count.items() if c > threshold]

