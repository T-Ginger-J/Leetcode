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

