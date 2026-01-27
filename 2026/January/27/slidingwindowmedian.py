from typing import List
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # max heap (invert values)
        large = []  # min heap
        delayed = defaultdict(int)

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            if len(small) > len(large) + 1:
                heapq.heappush(large, -heapq.heappop(small))
                prune(small)
            elif len(small) < len(large):
                heapq.heappush(small, -heapq.heappop(large))
                prune(large)

        for i in range(k):
            heapq.heappush(small, -nums[i])
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))

        res = []

        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(-small[0]))
            else:
                res.append((-small[0] + large[0]) / 2.0)

            if i == len(nums):
                break

            out_num = nums[i - k]
            in_num = nums[i]

            if out_num <= -small[0]:
                delayed[out_num] += 1
                if out_num == -small[0]:
                    prune(small)
            else:
                delayed[out_num] += 1
                if large and out_num == large[0]:
                    prune(large)

            if in_num <= -small[0]:
                heapq.heappush(small, -in_num)
            else:
                heapq.heappush(large, in_num)

            balance()

        return res
