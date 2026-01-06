// LeetCode 205: Isomorphic Strings
// Explanation:
// 1. Use two arrays to store mapping from s→t and t→s.
// 2. Validate bijection by ensuring consistent mapping both ways.
// Time Complexity: O(n)
// Space Complexity: O(1) (constant 256 chars)

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.size() != t.size()) return false;
        vector<int> mapS(256, -1), mapT(256, -1);
        for (int i = 0; i < s.size(); ++i) {
            if (mapS[s[i]] == -1 && mapT[t[i]] == -1) {
                mapS[s[i]] = t[i];
                mapT[t[i]] = s[i];
            } else if (mapS[s[i]] != t[i] || mapT[t[i]] != s[i]) {
                return false;
            }
        }
        return true;
    }
};

/*
Solution sol;
cout << boolalpha;
cout << sol.isIsomorphic("egg", "add") << endl;    // true
cout << sol.isIsomorphic("foo", "bar") << endl;    // false
cout << sol.isIsomorphic("paper", "title") << endl;// true
*/