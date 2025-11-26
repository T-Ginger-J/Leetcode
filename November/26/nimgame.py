# LeetCode 292: Nim Game
# Explanation:
# 1. The game: two players take 1-3 stones, and the player who removes the last stone wins.
# 2. Key observation: if n % 4 == 0, the current player will always lose if the opponent plays optimally.
# 3. Otherwise, the current player can always force a win by leaving a multiple of 4.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
