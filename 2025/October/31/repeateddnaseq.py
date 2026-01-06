# LeetCode 187: Repeated DNA Sequences
# Explanation:
# 1. Use a sliding window of size 10 to extract substrings.
# 2. Keep track of seen substrings in a set.
# 3. If a substring is seen again, add it to the repeated set.
# 4. Return all repeated substrings as a list.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)
        return list(repeated)

    def findRepeatedDnaSequencesBitEncoding(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen, repeated = set(), set()
        num = 0
        for i, ch in enumerate(s):
            num = ((num << 2) | mapping[ch]) & ((1 << 20) - 1)
            if i >= 9:
                if num in seen:
                    repeated.add(s[i-9:i+1])
                else:
                    seen.add(num)
        return list(repeated)
    
    def findRepeatedDnaSequencesOneLine(self, s: str) -> list[str]:
        return list({s[i:i+10] for i in range(len(s)-9)} & {s[j:j+10] for j in range(1, len(s)-8)})
    
sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# ["AAAAACCCCC", "CCCCCAAAAA"]

print(sol.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
# ["AAAAAAAAAA"]

print(sol.findRepeatedDnaSequences("ACGTACGTAC"))
# []
