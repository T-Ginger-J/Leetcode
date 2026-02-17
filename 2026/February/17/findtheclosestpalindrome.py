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

