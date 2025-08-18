def length_of_longest_substring(s: str) -> int:
    chars = set()  # to track unique characters in current window
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        # if duplicate, shrink window from the left
        while c in chars:
            chars.remove(s[left])
            left += 1
        
        chars.add(c)
        max_len = max(max_len, right - left + 1)

    return max_len

# --- Example usage ---
s = "abcabcbb"
print("Longest substring length:", length_of_longest_substring(s))  # Output: 3
