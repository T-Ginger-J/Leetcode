class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        threshold = len(nums) // 3
        return [x for x, c in count.items() if c > threshold]

    def majorityElementOneLine(self, nums: list[int]) -> list[int]:
        return [x for x in set(nums) if nums.count(x) > len(nums)//3]

