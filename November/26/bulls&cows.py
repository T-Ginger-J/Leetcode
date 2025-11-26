# LeetCode 299: Bulls and Cows
# Explanation:
# 1. Bulls: digits in secret and guess match in both value and position.
# 2. Cows: digits in secret and guess match in value but not in position.
# 3. Iterate through both strings:
#    - If secret[i] == guess[i], increment bulls.
#    - Otherwise, count occurrences of digits in secret and guess.
# 4. For cows, sum the min count of each digit that is not a bull.
# Time Complexity: O(n), iterate once through strings
# Space Complexity: O(10), storing digit counts (constant space)

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        from collections import Counter
        s_count = Counter()
        g_count = Counter()
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                s_count[s] += 1
                g_count[g] += 1
        for digit in s_count:
            cows += min(s_count[digit], g_count.get(digit, 0))
        return f"{bulls}A{cows}B"

