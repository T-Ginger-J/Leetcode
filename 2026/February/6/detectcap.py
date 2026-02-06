# LeetCode 520: Detect Capital
# Explanation:
# 1. Given a word, determine if capitalization is used correctly.
# 2. Valid cases:
#    - All letters are uppercase (e.g., "USA")
#    - All letters are lowercase (e.g., "leetcode")
#    - Only the first letter is uppercase (e.g., "Google")
# 3. Any other pattern is invalid.

# Methods Used:
# - Built-in String Checks
# - Manual Character Inspection

# Time Complexity:
# - O(n), n = length of the word

# Space Complexity:
# - O(1)


class Solution:

    # -------------------------------------------------------
    # Method 1: Using Built-in Functions (Optimal)
    # -------------------------------------------------------
    def detectCapitalUseBuiltIn(self, word: str) -> bool:

        return (
            word.isupper() or
            word.islower() or
            (word[0].isupper() and word[1:].islower())
        )

    # -------------------------------------------------------
    # Method 2: Manual Counting
    # -------------------------------------------------------
    def detectCapitalUseManual(self, word: str) -> bool:

        upper = 0

        for ch in word:
            if 'A' <= ch <= 'Z':
                upper += 1

        n = len(word)

        # All uppercase
        if upper == n:
            return True

        # All lowercase
        if upper == 0:
            return True

        # Only first uppercase
        if upper == 1 and 'A' <= word[0] <= 'Z':
            return True

        return False

    # -------------------------------------------------------
    # Default Method
    # -------------------------------------------------------
    def detectCapitalUse(self, word: str) -> bool:
        return self.detectCapitalUseBuiltIn(word)


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
print(Solution().detectCapitalUse("USA"))      # True

# Example 2
print(Solution().detectCapitalUse("leetcode"))  # True

# Example 3
print(Solution().detectCapitalUse("Google"))   # True

# Example 4 (Invalid)
print(Solution().detectCapitalUse("FlaG"))     # False

# Example 5 (Single Character)
print(Solution().detectCapitalUse("A"))        # True
print(Solution().detectCapitalUse("z"))        # True
