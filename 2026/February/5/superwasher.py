# LeetCode 517: Super Washing Machines
# Explanation:
# 1. Each machine has some dresses.
# 2. We want all machines to reach the same target.
# 3. Use prefix balance to track surplus/deficit.
# 4. The maximum imbalance determines the answer.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List


class Solution:

    # -------------------------------------------------------
    # Greedy Prefix Balance (Optimal)
    # -------------------------------------------------------
    def findMinMoves(self, machines: List[int]) -> int:

        total = sum(machines)
        n = len(machines)

        # Impossible
        if total % n != 0:
            return -1

        target = total // n

        balance = 0
        ans = 0

        for load in machines:

            diff = load - target
            balance += diff

            # Track maximum required moves
            ans = max(
                ans,
                abs(balance),
                diff
            )

        return ans


# -------------------------------------------------------
# Examples
# -------------------------------------------------------

print(Solution().findMinMoves([1, 0, 5]))      # 3
print(Solution().findMinMoves([0, 2, 0]))      # -1
print(Solution().findMinMoves([2, 2, 2]))      # 0
print(Solution().findMinMoves([10, 0, 0, 0]))  # 6
# LeetCode 517: Super Washing Machines
# Explanation:
# 1. Each machine has some dresses.
# 2. We want all machines to reach the same target.
# 3. Use prefix balance to track surplus/deficit.
# 4. The maximum imbalance determines the answer.

# Time Complexity: O(n)
# Space Complexity: O(1)


from typing import List


class Solution:

    # -------------------------------------------------------
    # Greedy Prefix Balance (Optimal)
    # -------------------------------------------------------
    def findMinMoves(self, machines: List[int]) -> int:

        total = sum(machines)
        n = len(machines)

        # Impossible
        if total % n != 0:
            return -1

        target = total // n

        balance = 0
        ans = 0

        for load in machines:

            diff = load - target
            balance += diff

            # Track maximum required moves
            ans = max(
                ans,
                abs(balance),
                diff
            )

        return ans


# -------------------------------------------------------
# Examples
# -------------------------------------------------------

print(Solution().findMinMoves([1, 0, 5]))      # 3
print(Solution().findMinMoves([0, 2, 0]))      # -1
print(Solution().findMinMoves([2, 2, 2]))      # 0
print(Solution().findMinMoves([10, 0, 0, 0]))  # 6
