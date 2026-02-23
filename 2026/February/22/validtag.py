# LeetCode 591: Tag Validator
# Explanation:
# 1. Use a stack to track open tags.
# 2. Parse from left to right.
# 3. Handle three valid patterns:
#    - Opening tag: <TAG>
#    - Closing tag: </TAG>
#    - CDATA: <![CDATA[...]]>
# 4. TAG must be 1–9 uppercase letters only.
# 5. Any invalid format immediately returns False.
# 6. All content must be inside one root tag.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isValid(self, code: str) -> bool:

        stack = []
        i = 0
        n = len(code)

        while i < n:

            # All content must be inside a tag (except at start)
            if i > 0 and not stack:
                return False

            # CDATA
            if code.startswith("<![CDATA[", i):

                if not stack:
                    return False

                j = code.find("]]>", i)
                if j == -1:
                    return False

                i = j + 3

            # Closing tag
            elif code.startswith("</", i):

                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i+2:j]

                # Must be 1–9 uppercase letters
                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                    return False

                if not stack or stack[-1] != tag:
                    return False

                stack.pop()
                i = j + 1

            # Opening tag
            elif code.startswith("<", i):

                j = code.find(">", i)
                if j == -1:
                    return False

                tag = code[i+1:j]

                # Reject nested '<' or invalid characters
                if not (1 <= len(tag) <= 9 and tag.isupper() and tag.isalpha()):
                    return False

                stack.append(tag)
                i = j + 1

            # Normal text
            else:
                i += 1

        return not stack


