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

