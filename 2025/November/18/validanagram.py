# LeetCode 242: Valid Anagram
#
# Explanation:
# Two strings are anagrams if they have the same character counts.
# Use a frequency dictionary (or array of size 26).
#
# Time Complexity: O(n)
# Space Complexity: O(1) for fixed alphabet, else O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for ch in s:
            count[ord(ch) - 97] += 1
        for ch in t:
            count[ord(ch) - 97] -= 1
            if count[ord(ch) - 97] < 0:
                return False

        return True

# Example usage:
# sol = Solution()
# print(sol.isAnagram("anagram", "nagaram")) # True
# print(sol.isAnagram("rat", "car"))         # False
