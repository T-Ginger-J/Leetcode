from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_prev = (i == 0) or (flowerbed[i-1] == 0)
                empty_next = (i == length-1) or (flowerbed[i+1] == 0)
                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
        return n <= 0
