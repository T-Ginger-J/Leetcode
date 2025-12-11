import bisect

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')

        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]

                # Find max subarray sum <= k
                prefix_sums = [0]
                cur_sum = 0
                for s in col_sums:
                    cur_sum += s
                    # We want cur_sum - prev >= -k -> prev >= cur_sum - k
                    i = bisect.bisect_left(prefix_sums, cur_sum - k)
                    if i < len(prefix_sums):
                        res = max(res, cur_sum - prefix_sums[i])
                    bisect.insort(prefix_sums, cur_sum)
        return res

