// LeetCode 214: Shortest Palindrome
// Explanation:
// 1. Use KMP-like prefix array to find longest palindrome prefix.
// 2. Add remaining reversed part in front.
// Time Complexity: O(n)
// Space Complexity: O(n)

var shortestPalindrome = function(s) {
    const rev = s.split('').reverse().join('');
    const str = s + '#' + rev;
    const lps = new Array(str.length).fill(0);

    for (let i = 1; i < str.length; i++) {
        let j = lps[i - 1];
        while (j > 0 && str[i] !== str[j]) j = lps[j - 1];
        if (str[i] === str[j]) j++;
        lps[i] = j;
    }

    return rev.slice(0, s.length - lps[str.length - 1]) + s;
};

console.log(shortestPalindrome("aacecaaa")); // "aaacecaaa"
console.log(shortestPalindrome("abcd"));     // "dcbabcd"
console.log(shortestPalindrome("race"));     // "ecarace"
