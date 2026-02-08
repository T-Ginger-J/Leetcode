# LeetCode 524: Longest Word in Dictionary through Deleting
# Explanation:
# 1. We are given a string s and a list of dictionary words.
# 2. We need the longest word that can be formed by deleting characters from s.
# 3. If multiple answers exist, return the smallest lexicographical one.
# 4. A word is valid if it is a subsequence of s.

# Methods Used:
# - Two-Pointer Subsequence Check
# - Sorting + Greedy Selection
# - Preprocessing with Next-Occurrence Table

# Time Complexity:
# - Two-Pointer: O(n * L)
#   n = number of words, L = length of s
# - Preprocessing: O(26 * L + n * m)

# Space Complexity:
# - O(1) for two-pointer
# - O(26 * L) for preprocessing


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Sorting + Two-Pointer (Optimal for Constraints)
    # -------------------------------------------------------
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        # Sort by length desc, lex asc
        dictionary.sort(key=lambda x: (-len(x), x))

        def isSubseq(word, s):
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            return i == len(word)

        for word in dictionary:
            if isSubseq(word, s):
                return word

        return ""

    # -------------------------------------------------------
    # Method 2: Preprocessing Next Occurrence
    # -------------------------------------------------------
    def findLongestWordNext(self, s: str, dictionary: List[str]) -> str:

        n = len(s)

        # next_pos[i][c] = next index of char c after i
        next_pos = [[-1] * 26 for _ in range(n + 1)]

        for c in range(26):
            next_pos[n][c] = -1

        for i in range(n - 1, -1, -1):

            next_pos[i] = next_pos[i + 1][:]

            next_pos[i][ord(s[i]) - 97] = i

        def isSubseq(word):

            idx = 0

            for ch in word:

                if idx == -1:
                    return False

                idx = next_pos[idx][ord(ch) - 97]

                if idx == -1:
                    return False

                idx += 1

            return True

        best = ""

        for word in dictionary:

            if isSubseq(word):

                if len(word) > len(best) or (
                    len(word) == len(best) and word < best
                ):
                    best = word

        return best


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
print(Solution().findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))  
# "apple"

# Example 2
print(Solution().findLongestWord("abpcplea", ["a", "b", "c"]))  
# "a"

# Example 3 (No Match)
print(Solution().findLongestWord("abc", ["d", "e", "f"]))  
# ""

# Example 4 (Lex Order Tie)
print(Solution().findLongestWord("bab", ["ba", "ab"]))  
# "ab"

# Example 5 (Empty Dictionary)
print(Solution().findLongestWord("abc", []))  
# ""
