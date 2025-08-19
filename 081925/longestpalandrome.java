class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) return "";

        // Transform the string: add boundaries
        StringBuilder t = new StringBuilder("^");
        for (char c : s.toCharArray()) {
            t.append("#").append(c);
        }
        t.append("#$");
        char[] T = t.toString().toCharArray();

        int n = T.length;
        int[] P = new int[n]; // Array to store palindrome radius
        int C = 0, R = 0;     // Current center and right boundary

        for (int i = 1; i < n - 1; i++) {
            int mirror = 2 * C - i;  // mirror of i around center C

            if (i < R) {
                P[i] = Math.min(R - i, P[mirror]);
            }

            // Expand palindrome centered at i
            while (T[i + 1 + P[i]] == T[i - 1 - P[i]]) {
                P[i]++;
            }

            // Update center if palindrome expands beyond R
            if (i + P[i] > R) {
                C = i;
                R = i + P[i];
            }
        }

        // Find longest palindrome
        int maxLen = 0, centerIndex = 0;
        for (int i = 1; i < n - 1; i++) {
            if (P[i] > maxLen) {
                maxLen = P[i];
                centerIndex = i;
            }
        }

        int start = (centerIndex - maxLen) / 2;  // Map back to original string
        return s.substring(start, start + maxLen);
    }
}
