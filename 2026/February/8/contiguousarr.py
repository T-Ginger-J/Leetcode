
    # -------------------------------------------------------
    # Method 1: Prefix Sum + Hash Map (Optimal)
    # -------------------------------------------------------
    def findMaxLength(self, nums: List[int]) -> int:

        prefix_sum = 0
        max_len = 0
        sum_index = {0: -1}  # sum -> earliest index

        for i, num in enumerate(nums):

            # Treat 0 as -1
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in sum_index:
                max_len = max(max_len, i - sum_index[prefix_sum])
            else:
                sum_index[prefix_sum] = i

        return max_len

