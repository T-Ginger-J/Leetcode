// LeetCode 451: Sort Characters By Frequency
// Method: Bucket Sort
// Time Complexity: O(n)
// Space Complexity: O(n)

var frequencySort = function(s) {
    const freq = {};
    for (const ch of s) {
        freq[ch] = (freq[ch] || 0) + 1;
    }

    const buckets = Array(s.length + 1).fill(0).map(() => []);
    for (const ch in freq) {
        buckets[freq[ch]].push(ch);
    }

    let res = "";
    for (let i = buckets.length - 1; i > 0; i--) {
        for (const ch of buckets[i]) {
            res += ch.repeat(i);
        }
    }
    return res;
};

