# LeetCode 564: Find the Closest Palindrome
# Explanation:
# 1. Given a string n representing an integer, find the closest integer (as string) that is a palindrome and not equal to n.
# 2. Approach:
#    - Generate candidates by:
#       a) Using the first half of n and mirroring it to form a palindrome.
#       b) Incrementing or decrementing the first half and mirroring.
#       c) Edge cases: 10^k + 1 or 10^(k-1) - 1 (like 100...001 or 99...9)
#    - Choose the candidate with minimum absolute difference to n.
#    - If tie, choose the smaller one.
# 3. Time Complexity: O(k), k = length of n
# 4. Space Complexity: O(k)

class Solution:

    # -------------------------------------------------------
    # Method 1: Construct candidates
    # -------------------------------------------------------
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        candidates = set()

        # Edge cases: 10^k +1 and 10^(k-1) -1
        candidates.add(str(10**length +1))
        candidates.add(str(10**(length-1) -1))

        prefix = int(n[:(length+1)//2])
        for i in [-1,0,1]:
            new_prefix = str(prefix + i)
            if length %2 == 0:
                pal = new_prefix + new_prefix[::-1]
            else:
                pal = new_prefix + new_prefix[:-1][::-1]
            candidates.add(pal)

        candidates.discard(n)
        closest = None
        min_diff = float('inf')
        for cand in candidates:
            if cand == '':  # skip empty
                continue
            diff = abs(int(cand) - num)
            if diff < min_diff or (diff == min_diff and int(cand) < int(closest)):
                min_diff = diff
                closest = cand
        return closest

    # -------------------------------------------------------
    # Method 2: Brute-force (inefficient)
    # -------------------------------------------------------
    def nearestPalindromicBrute(self, n: str) -> str:
        num = int(n)
        offset = 1
        while True:
            if str(num - offset) == str(num - offset)[::-1] and num - offset != num:
                return str(num - offset)
            if str(num + offset) == str(num + offset)[::-1] and num + offset != num:
                return str(num + offset)
            offset +=1


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
n1 = "123"
print(sol.nearestPalindromic(n1))           # "121"
print(sol.nearestPalindromicBrute(n1))      # "121"

# Example 2: palindrome number
n2 = "1"
print(sol.nearestPalindromic(n2))           # "0"

# Example 3: edge 1000
n3 = "1000"
print(sol.nearestPalindromic(n3))           # "999"

# Example 4: tie (choose smaller)
n4 = "10"
print(sol.nearestPalindromic(n4))           # "9"

# Example 5: even length
n5 = "1234"
print(sol.nearestPalindromic(n5))           # "1221"
