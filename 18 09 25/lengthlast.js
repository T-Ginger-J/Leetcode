// LeetCode 58: Length of Last Word
// Explanation:
// 1. trim() removes trailing/leading spaces
// 2. Iterate from end to count last word length
// Time Complexity: O(n)

var lengthOfLastWord = function(s) {
    s = s.trim();
    let i = s.length - 1, length = 0;
    while (i >= 0 && s[i] !== ' ') {
        length++;
        i--;
    }
    return length;
};

// Example usage:
// console.log(lengthOfLastWord("Hello World"));            // 5
// console.log(lengthOfLastWord("   fly me   to   the moon  ")); // 4
// console.log(lengthOfLastWord("a"));                      // 1
