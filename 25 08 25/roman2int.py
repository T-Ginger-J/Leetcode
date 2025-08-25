VALUES = {
    'I': 1, 'V': 5, 'X': 10,
    'L': 50, 'C': 100, 'D': 500, 'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            val = VALUES[s[i]]
            if val < prev:
                total -= val
            else:
                total += val
            prev = val
        return total
