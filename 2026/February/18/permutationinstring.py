# LeetCode 567: Permutation in String
# Explanation:
# 1. Given two strings s1 and s2, check if s2 contains a permutation of s1 as a substring.
# 2. Approach:
#    - Use sliding window of length len(s1) over s2.
#    - Maintain frequency count of s1 and current window in s2.
#    - If counts match, return True.
# 3. Time Complexity: O(n), n = len(s2)
# 4. Space Complexity: O(1) (fixed size array of 26 for lowercase letters)

from collections import Counter

class Solution:

    # -------------------------------------------------------
    # Method 1: Sliding window with Counter
    # -------------------------------------------------------
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        count_s1 = Counter(s1)
        count_window = Counter()

        for i, ch in enumerate(s2):
            count_window[ch] += 1
            if i >= len_s1:
                left = s2[i - len_s1]
                count_window[left] -= 1
                if count_window[left] == 0:
                    del count_window[left]
            if count_window == count_s1:
                return True
        return False

    # -------------------------------------------------------
    # Method 2: Sliding window with fixed-size array
    # -------------------------------------------------------
    def checkInclusionArray(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from itertools import accumulate

        freq1 = [0]*26
        freq2 = [0]*26
        for ch in s1:
            freq1[ord(ch)-ord('a')] +=1
        for ch in s2[:len(s1)]:
            freq2[ord(ch)-ord('a')] +=1
        if freq1 == freq2:
            return True
        for i in range(len(s1), len(s2)):
            freq2[ord(s2[i])-ord('a')] +=1
            freq2[ord(s2[i-len(s1)])-ord('a')] -=1
            if freq1 == freq2:
                return True
        return False
