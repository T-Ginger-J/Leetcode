// LeetCode 87: Scramble String
// Explanation:
// 1. Use recursion + memoization to check if s2 is scrambled version of s1.
// 2. Check equal strings, sorted mismatch, and try all partitions.
// Time Complexity: O(n^4)
// Space Complexity: O(n^3)

using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<string, bool> memo = new Dictionary<string, bool>();

    public bool IsScramble(string s1, string s2) {
        string key = s1 + "|" + s2;
        if (memo.ContainsKey(key)) return memo[key];
        if (s1 == s2) return memo[key] = true;
        char[] a = s1.ToCharArray(), b = s2.ToCharArray();
        Array.Sort(a); Array.Sort(b);
        if (new string(a) != new string(b)) return memo[key] = false;

        int n = s1.Length;
        for (int i = 1; i < n; i++) {
            if ((IsScramble(s1.Substring(0, i), s2.Substring(0, i)) &&
                 IsScramble(s1.Substring(i), s2.Substring(i))) ||
                (IsScramble(s1.Substring(0, i), s2.Substring(n - i)) &&
                 IsScramble(s1.Substring(i), s2.Substring(0, n - i)))) {
                return memo[key] = true;
            }
        }
        return memo[key] = false;
    }
}

// Example usage:
// var sol = new Solution();
// Console.WriteLine(sol.IsScramble("great", "rgeat")); // True
// Console.WriteLine(sol.IsScramble("abcde", "caebd")); // False
// Console.WriteLine(sol.IsScramble("a", "a"));         // True
