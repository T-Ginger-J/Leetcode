class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for p in parts:
                if not p.isdigit():
                    return "Neither"
                if (p[0] == '0' and len(p) > 1) or not (0 <= int(p) <= 255):
                    return "Neither"
            return "IPv4"

        if queryIP.count(':') == 7:
            parts = queryIP.split(':')
            if len(parts) != 8:
                return "Neither"
            hex_digits = set("0123456789abcdefABCDEF")
            for p in parts:
                if not (1 <= len(p) <= 4):
                    return "Neither"
                for c in p:
                    if c not in hex_digits:
                        return "Neither"
            return "IPv6"

        return "Neither"

