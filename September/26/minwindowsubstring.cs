// LeetCode 76: Minimum Window Substring
// Explanation:
// 1. Use sliding window with two pointers.
// 2. Track counts of chars from t using dictionaries.
// 3. Expand and contract window to find min substring.
// Time Complexity: O(|s| + |t|)
// Space Complexity: O(|s| + |t|)

using System;
using System.Collections.Generic;

public class Solution {
    public string MinWindow(string s, string t) {
        if (string.IsNullOrEmpty(s) || string.IsNullOrEmpty(t)) return "";
        
        var need = new Dictionary<char,int>();
        foreach (var c in t) {
            if (!need.ContainsKey(c)) need[c] = 0;
            need[c]++;
        }

        var have = new Dictionary<char,int>();
        int required = need.Count, formed = 0;
        int l = 0, r = 0, minLen = Int32.MaxValue, start = 0;

        while (r < s.Length) {
            char c = s[r];
            if (!have.ContainsKey(c)) have[c] = 0;
            have[c]++;
            
            if (need.ContainsKey(c) && have[c] == need[c]) formed++;

            while (l <= r && formed == required) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    start = l;
                }
                have[s[l]]--;
                if (need.ContainsKey(s[l]) && have[s[l]] < need[s[l]]) formed--;
                l++;
            }
            r++;
        }

        return minLen == Int32.MaxValue ? "" : s.Substring(start, minLen);
    }
}

// Example usage:
// var sol = new Solution();
// Console.WriteLine(sol.MinWindow("ADOBECODEBANC", "ABC")); // "BANC"
// Console.WriteLine(sol.MinWindow("a", "a"));               // "a"
// Console.WriteLine(sol.MinWindow("a", "aa"));              // ""
