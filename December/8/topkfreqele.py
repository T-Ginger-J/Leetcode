# LeetCode 347: Top K Frequent Elements (Bucket Sort)
# Explanation:
# 1. Count frequency of each number.
# 2. Create buckets where index i stores numbers occurring i times.
# 3. Traverse buckets backwards and collect k most frequent numbers.
# Time Complexity: O(n)
# Space Complexity: O(n)

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

    def topKFrequentMinHeap(self, nums, k):
        from collections import Counter
        import heapq

        freq = Counter(nums)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for (count, num) in heap]
    
print(Solution().topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
print(Solution().topKFrequent([1], 1))            # Output: [1]
