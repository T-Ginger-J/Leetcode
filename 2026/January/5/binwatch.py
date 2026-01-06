# LeetCode 401: Binary Watch
# Explanation:
# 1. Iterate over all possible hours (0-11) and minutes (0-59)
# 2. Count the number of 1s in binary
# 3. If total equals turnedOn, add to result
# Time Complexity: O(12*60)
# Space Complexity: O(1) extra

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res

print(Solution().readBinaryWatch(1))
# Output: ['0:01','0:02','0:04','0:08','0:16','0:32','1:00','2:00','4:00','8:00']
