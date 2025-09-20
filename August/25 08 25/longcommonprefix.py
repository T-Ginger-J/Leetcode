class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first word as prefix
        prefix = strs[0]
        
        # Compare prefix with each word
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
