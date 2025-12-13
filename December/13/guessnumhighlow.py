class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 0:
                high = mid - 1
            else:
                low = mid + 1

