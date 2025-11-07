# LeetCode 205: Isomorphic Strings
# Explanation:
# 1. Maintain two maps to store character mappings from s→t and t→s.
# 2. Ensure one-to-one correspondence between both.
# 3. If mismatch found, return False.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t, map_t_s = {}, {}
        for c1, c2 in zip(s, t):
            if (c1 in map_s_t and map_s_t[c1] != c2) or (c2 in map_t_s and map_t_s[c2] != c1):
                return False
            map_s_t[c1] = c2
            map_t_s[c2] = c1
        return True

    def isIsomorphicOneLine(self, s: str, t: str) -> bool:
        return [s.index(c) for c in s] == [t.index(c) for c in t]
    
sol = Solution()
print(sol.isIsomorphic("egg", "add"))    # True
print(sol.isIsomorphic("foo", "bar"))    # False
print(sol.isIsomorphic("paper", "title"))# True

