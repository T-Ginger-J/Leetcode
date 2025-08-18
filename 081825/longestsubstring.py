def length_of_longest_substring(s: str) -> int:
    char_index = {}  # map character -> last seen index
    left = 0
    max_len = 0

    for right, c in enumerate(s):
        # if character seen before and inside current window, move left
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        
        char_index[c] = right  # update last seen index
        max_len = max(max_len, right - left + 1)

    return max_len

# --- Example usage ---
s = "abcabcbb"
print("Longest substring length:", length_of_longest_substring(s))  # Output: 3


