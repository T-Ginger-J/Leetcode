# LeetCode 420: Strong Password Checker
# Explanation:
# 1. Count missing types (lower, upper, digit)
# 2. Count sequences of repeats and required replacements
# 3. Handle length <6, 6-20, >20 differently
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing_lower = missing_upper = missing_digit = 1
        for c in password:
            if c.islower(): missing_lower = 0
            elif c.isupper(): missing_upper = 0
            elif c.isdigit(): missing_digit = 0
        missing_types = missing_lower + missing_upper + missing_digit

        # find repeating sequences
        repeats = []
        i = 2
        while i < n:
            if password[i] == password[i-1] == password[i-2]:
                start = i-2
                while i < n and password[i] == password[i-1]:
                    i += 1
                repeats.append(i-start)
            else:
                i += 1

        if n < 6:
            return max(missing_types, 6 - n)
        elif n <= 20:
            replace = sum(length // 3 for length in repeats)
            return max(missing_types, replace)
        else:
            delete = n - 20
            # First pass: mod 0
            for i in range(len(repeats)):
                if delete <= 0: break
                if repeats[i] < 3: continue
                if repeats[i] % 3 == 0:
                    remove = min(delete, 1)
                    repeats[i] -= remove
                    delete -= remove
            # Second pass: mod 1
            for i in range(len(repeats)):
                if delete <= 0: break
                if repeats[i] < 3: continue
                if repeats[i] % 3 == 1:
                    remove = min(delete, 2)
                    repeats[i] -= remove
                    delete -= remove
            # Third pass: mod 2
            for i in range(len(repeats)):
                if delete <= 0: break
                if repeats[i] < 3: continue
                if repeats[i] % 3 == 2 or repeats[i] % 3 == 0 or repeats[i] % 3 == 1:
                    remove = min(delete, repeats[i]-2)
                    repeats[i] -= remove
                    delete -= remove

            replace = sum(length // 3 for length in repeats)
            return (n - 20) + max(missing_types, replace)


print(Solution().strongPasswordChecker("a"))           # Output: 5
print(Solution().strongPasswordChecker("aA1"))         # Output: 3
print(Solution().strongPasswordChecker("1337C0d3"))    # Output: 0
