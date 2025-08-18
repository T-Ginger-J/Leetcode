#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

int lengthOfLongestSubstring(string s) {
    unordered_set<char> chars; // to track unique characters in current window
    int left = 0, maxLen = 0;

    for (int right = 0; right < s.length(); right++) {
        // if duplicate, shrink window from left
        while (chars.count(s[right])) {
            chars.erase(s[left]);
            left++;
        }

        chars.insert(s[right]);
        maxLen = max(maxLen, right - left + 1);
    }

    return maxLen;
}

// --- Example usage ---
int main() {
    string s = "abcabcbb";
    cout << "Longest substring length: " << lengthOfLongestSubstring(s) << endl;
    return 0;
}