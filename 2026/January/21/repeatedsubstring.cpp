#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int n = s.size();
        for (int len = 1; len <= n / 2; len++) {
            if (n % len != 0) continue;
            string sub = s.substr(0, len);
            bool match = true;
            for (int i = len; i < n; i += len) {
                if (s.substr(i, len) != sub) {
                    match = false;
                    break;
                }
            }
            if (match) return true;
        }
        return false;
    }
};

int main() {
    Solution sol;

    // Example 1: Simple repeat
    cout << sol.repeatedSubstringPattern("abab") << endl; // Expected: 1 (true)

    // Example 2: Single character repeated
    cout << sol.repeatedSubstringPattern("aaaa") << endl; // Expected: 1 (true)

    // Example 3: No repeat
    cout << sol.repeatedSubstringPattern("abc") << endl; // Expected: 0 (false)

    // Example 4: Two repeats but not complete
    cout << sol.repeatedSubstringPattern("aba") << endl; // Expected: 0 (false)

    return 0;
}
