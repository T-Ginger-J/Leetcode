// LeetCode 187: Repeated DNA Sequences
// Explanation:
// 1. Slide a window of length 10 across the string.
// 2. Keep track of seen substrings in a Set.
// 3. If a substring repeats, store it in another Set.
// 4. Return all repeated substrings as an array.
// Time Complexity: O(n)
// Space Complexity: O(n)

var findRepeatedDnaSequences = function(s) {
    const seen = new Set();
    const repeated = new Set();
    for (let i = 0; i + 9 < s.length; i++) {
        const seq = s.substring(i, i + 10);
        if (seen.has(seq)) repeated.add(seq);
        else seen.add(seq);
    }
    return Array.from(repeated);
};

console.log(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"));
// ["AAAAACCCCC", "CCCCCAAAAA"]

console.log(findRepeatedDnaSequences("AAAAAAAAAAAAA"));
// ["AAAAAAAAAA"]

console.log(findRepeatedDnaSequences("ACGTACGTAC"));
// []
