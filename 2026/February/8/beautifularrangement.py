class Solution:

    # -------------------------------------------------------
    # Method 1: Backtracking (Optimal)
    # -------------------------------------------------------
    def countArrangement(self, n: int) -> int:

        def backtrack(pos, used):
            if pos > n:
                return 1

            count = 0

            for num in range(1, n + 1):

                if not used[num] and (num % pos == 0 or pos % num == 0):

                    used[num] = True
                    count += backtrack(pos + 1, used)
                    used[num] = False

            return count

        used = [False] * (n + 1)
        return backtrack(1, used)


