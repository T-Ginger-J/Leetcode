# LeetCode 552: Student Attendance Record II
# Explanation:
# 1. Count the number of attendance records of length n that are eligible for an award.
# 2. Conditions:
#    - Fewer than 2 'A's in the string.
#    - No more than 2 consecutive 'L's.
# 3. Approach:
#    - Use Dynamic Programming to track states:
#       dp[i][a][l] = number of strings of length i with 'a' absences and ending with l consecutive L's.
#    - Transition:
#       - Add 'P': dp[i][a][0] += sum(dp[i-1][a][0..2])
#       - Add 'L': dp[i][a][l+1] += dp[i-1][a][l] (only if l<2)
#       - Add 'A': dp[i][1][0] += sum(dp[i-1][0][0..2]) (only if a=0)
# 4. Time Complexity: O(n)
# 5. Space Complexity: O(n*2*3) = O(n)

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

    # -------------------------------------------------------
    # Method 2: Optimized DP with 1D arrays (space O(6))
    # -------------------------------------------------------
    def checkRecordIIOptimized(self, n: int) -> int:
        MOD = 10**9 + 7
        # states: (a, l) -> total 2*3 = 6 states
        curr = [0]*6
        curr[0] = 1  # (0A,0L)
        for _ in range(1, n+1):
            next_dp = [0]*6
            for state in range(6):
                a = state // 3
                l = state % 3
                # Add P
                next_dp[a*3+0] = (next_dp[a*3+0] + curr[state]) % MOD
                # Add L
                if l < 2:
                    next_dp[a*3+(l+1)] = (next_dp[a*3+(l+1)] + curr[state]) % MOD
                # Add A
                if a == 0:
                    next_dp[1*3+0] = (next_dp[1*3+0] + curr[state]) % MOD
            curr = next_dp
        return sum(curr) % MOD


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1: n = 1
print(sol.checkRecordII(1))           # 3 ("P","L","A")
print(sol.checkRecordIIOptimized(1))  # 3

# Example 2: n = 2
print(sol.checkRecordII(2))           # 8
print(sol.checkRecordIIOptimized(2))  # 8

# Example 3: n = 3
print(sol.checkRecordII(3))           # 19
print(sol.checkRecordIIOptimized(3))  # 19

# Example 4: n = 0
print(sol.checkRecordII(0))           # 1 (empty string)
print(sol.checkRecordIIOptimized(0))  # 1

# Example 5: Large n
print(sol.checkRecordIIOptimized(10)) # 3536
