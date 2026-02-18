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

