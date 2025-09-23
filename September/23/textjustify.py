# LeetCode 68: Text Justification
# Explanation:
# 1. Greedily pick words that fit within maxWidth.
# 2. If it's the last line or only one word, left-justify.
# 3. Otherwise, distribute spaces evenly across gaps.
# Time Complexity: O(n * L) where n = number of words, L = maxWidth
# Space Complexity: O(1)

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
    
    def fullJustifyOptimized(self, words: list[str], maxWidth: int) -> list[str]:
        res, i = [], 0
        while i < len(words):
            line_len, j = len(words[i]), i + 1
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            spaces, extra = maxWidth - line_len, j - i - 1
            if j == len(words) or extra == 0:
                res.append(" ".join(words[i:j]).ljust(maxWidth))
            else:
                space, rem = divmod(spaces, extra)
                line = ""
                for k in range(extra):
                    line += words[i + k] + " " * (space + (1 if k < rem else 0))
                line += words[j - 1]
                res.append(line)
            i = j
        return res
    
    fullJustifyOneLine=lambda s,w,m:[(lambda L:(L.ljust(m)if i==len(w)or len(ws)==1 else''.join(ws[k]+(' '*(m-len(''.join(ws))//(len(ws)-1)+(1 if k<(m-len(''.join(ws)))%(len(ws)-1)else 0)))for k in range(len(ws)-1))+ws[-1]))(' '.join(ws))for i in range(len(w))if not(i and sum(map(len,ws:=[w[i-1]]))+(len(ws)-1)>=m)]

