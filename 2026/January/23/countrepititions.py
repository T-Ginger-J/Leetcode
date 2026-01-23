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
