# LeetCode 273: Integer to English Words
# Explanation:
# 1. Break the number into chunks of thousands: billions, millions, thousands, remainder.
# 2. Convert each chunk using a helper that handles numbers < 1000.
# 3. Combine the words with the correct scale ("Thousand", "Million", "Billion").
#
# Time Complexity: O(1)  -- max 10 digits
# Space Complexity: O(1)

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine",
                    "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen",
                    "Seventeen","Eighteen","Nineteen"]

        tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        thousands = ["","Thousand","Million","Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

# Example usage:
# sol = Solution()
# print(sol.numberToWords(123))            # "One Hundred Twenty Three"
# print(sol.numberToWords(12345))          # "Twelve Thousand Three Hundred Forty Five"
# print(sol.numberToWords(1234567))        # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
