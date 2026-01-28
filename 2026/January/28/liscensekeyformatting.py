class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        res = []
        count = 0

        for ch in reversed(s):
            if count == k:
                res.append("-")
                count = 0
            res.append(ch)
            count += 1

        return "".join(reversed(res))


