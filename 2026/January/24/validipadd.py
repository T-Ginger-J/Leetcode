# LeetCode 468: Validate IP Address
# Explanation:
# Given a string queryIP, determine whether it is a valid IPv4 address,
# a valid IPv6 address, or neither.
#
# IPv4 Rules:
# - Consists of 4 decimal numbers separated by dots.
# - Each number is between 0 and 255.
# - No leading zeros unless the number is exactly "0".
#
# IPv6 Rules:
# - Consists of 8 hexadecimal numbers separated by colons.
# - Each group has 1 to 4 hex digits.
# - Hex digits are 0-9, a-f, A-F.
#
# Method 1: Manual Parsing (Optimal)
# - Split by '.' or ':' depending on format.
# - Validate each segment based on IP version rules.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

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

