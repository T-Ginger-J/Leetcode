// LeetCode 65: Valid Number
// Explanation:
// 1. Use flags to track digit, decimal, and exponent positions.
// 2. Validate step by step similar to a finite state machine.
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
    bool isNumber(string s) {
        int n = s.size();
        int i = 0;
        while (i < n && isspace(s[i])) i++; // trim leading spaces
        if (i < n && (s[i] == '+' || s[i] == '-')) i++; // sign

        bool num = false, dot = false, exp = false;

        for (; i < n; i++) {
            if (isdigit(s[i])) {
                num = true;
            } else if (s[i] == '.') {
                if (dot || exp) return false;
                dot = true;
            } else if (s[i] == 'e' || s[i] == 'E') {
                if (exp || !num) return false;
                exp = true;
                num = false;
                if (i+1 < n && (s[i+1] == '+' || s[i+1] == '-')) i++;
            } else if (isspace(s[i])) {
                while (i < n && isspace(s[i])) i++;
                return i == n && num;
            } else {
                return false;
            }
        }
        return num;
    }
};

