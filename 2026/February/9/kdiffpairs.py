class Solution:

    # -------------------------------------------------------
    # Method 1: Hash Map Counting (Optimal)
    # -------------------------------------------------------
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0  # absolute difference can't be negative

        count = 0
        freq = Counter(nums)

        if k == 0:
            # Count numbers appearing at least twice
            for val in freq.values():
                if val >= 2:
                    count += 1
        else:
            # Count unique nums where num+k exists
            for num in freq:
                if num + k in freq:
                    count += 1

        return count
