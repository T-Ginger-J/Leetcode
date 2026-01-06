# LeetCode 354: Russian Doll Envelopes
# Explanation:
# 1. Sort envelopes by width asc, height desc.
# 2. Find LIS on heights.
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        import bisect
        lis = []
        for _, h in envelopes:
            idx = bisect.bisect_left(lis, h)
            if idx == len(lis):
                lis.append(h)
            else:
                lis[idx] = h
        return len(lis)

envelopes = [[5,4],[6,4],[6,7],[2,3]]
print(Solution().maxEnvelopes(envelopes))  # Output: 3 (sequence: [2,3] -> [5,4] -> [6,7])

envelopes = [[1,1],[1,1],[1,1]]
print(Solution().maxEnvelopes(envelopes))  # Output: 1
