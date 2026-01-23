# LeetCode 466: Count The Repetitions
# Explanation:
# Given strings s1 and s2, and integers n1 and n2, define:
#   S1 = s1 repeated n1 times
#   S2 = s2 repeated n2 times
# Return the maximum integer M such that S2 repeated M times can be obtained
# from S1 by deleting characters (i.e., S2^M is a subsequence of S1).
#
# Method 1: Cycle Detection with Greedy Matching (Optimal)
# - Simulate matching s2 inside repeated s1.
# - Track the position in s2 after each full s1 scan.
# - Once a previously seen s2 position repeats, a cycle is detected.
# - Use math to skip full cycles efficiently.
#
# Time Complexity: O(len(s1) * len(s2))
# Space Complexity: O(len(s2))

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        index_map = {}
        s2_index = 0
        s2_count = 0
        s1_count = 0

        while s1_count < n1:
            s1_count += 1
            for c in s1:
                if c == s2[s2_index]:
                    s2_index += 1
                    if s2_index == len(s2):
                        s2_index = 0
                        s2_count += 1

            if s2_index in index_map:
                prev_s1_count, prev_s2_count = index_map[s2_index]
                cycle_len = s1_count - prev_s1_count
                cycle_s2 = s2_count - prev_s2_count

                remaining = n1 - s1_count
                cycles = remaining // cycle_len

                s1_count += cycles * cycle_len
                s2_count += cycles * cycle_s2
            else:
                index_map[s2_index] = (s1_count, s2_count)

        return s2_count // n2
