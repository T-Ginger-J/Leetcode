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
