class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter

        freq = Counter(nums)

        # Bucket: index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        result = []
        # Traverse buckets from highest frequency to lowest
        for count in range(len(buckets)-1, 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result

