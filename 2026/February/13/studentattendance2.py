class Solution:

    # -------------------------------------------------------
    # Method 1: Dynamic Programming
    # -------------------------------------------------------
    def checkRecordII(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp[i][a][l] -> length i, a absences, l consecutive L's
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]
        dp[0][0][0] = 1

        for i in range(1, n+1):
            for a in range(2):
                for l in range(3):
                    # Add P
                    dp[i][a][0] = (dp[i][a][0] + dp[i-1][a][l]) % MOD
                    # Add L
                    if l < 2:
                        dp[i][a][l+1] = (dp[i][a][l+1] + dp[i-1][a][l]) % MOD
                # Add A
                if a == 1:
                    for l in range(3):
                        dp[i][a][0] = (dp[i][a][0] + dp[i-1][0][l]) % MOD

        return sum(dp[n][a][l] for a in range(2) for l in range(3)) % MOD

