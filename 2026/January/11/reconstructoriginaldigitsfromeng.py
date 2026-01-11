# LeetCode 423: Reconstruct Original Digits from English
# Explanation:
# 1. Count frequency of each letter in the string.
# 2. Some digits have unique identifying letters:
#    - 'z' -> "zero" (0)
#    - 'w' -> "two" (2)
#    - 'u' -> "four" (4)
#    - 'x' -> "six" (6)
#    - 'g' -> "eight" (8)
# 3. After counting these, remove their letters from the total.
# 4. Then handle the remaining digits:
#    - 'o' -> "one" (1)  [after 0,2,4]
#    - 'h' -> "three" (3) [after 8]
#    - 'f' -> "five" (5)  [after 4]
#    - 's' -> "seven" (7) [after 6]
#    - 'i' -> "nine" (9)  [after 5,6,8]
# 5. Construct the final digit string in ascending order.

from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        out = {}
        
        out['0'] = count['z']
        out['2'] = count['w']
        out['4'] = count['u']
        out['6'] = count['x']
        out['8'] = count['g']
        
        out['3'] = count['h'] - out['8']
        out['5'] = count['f'] - out['4']
        out['7'] = count['s'] - out['6']
        out['1'] = count['o'] - out['0'] - out['2'] - out['4']
        out['9'] = count['i'] - out['5'] - out['6'] - out['8']
        
        result = [k * out[k] for k in sorted(out.keys())]
        return ''.join(result)
