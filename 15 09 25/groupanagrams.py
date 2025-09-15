from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

    def groupAnagramsTuple(self, strs):
        groups = defaultdict(list)
        for s in strs:
            key = tuple([0]*26)
            # make a list so we can increment
            counts = [0]*26
            for c in s:
                counts[ord(c)-97] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())

    def groupAnagramsOneLine(self, strs):
        return list({tuple(sorted(s)): [t for t in strs if sorted(t)==sorted(s)] for s in strs}.values())

sol = Solution()

# Example 1
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# Example 2
print(sol.groupAnagrams([""]))
# Output: [[""]]

# Example 3
print(sol.groupAnagrams(["a"]))
# Output: [["a"]]
