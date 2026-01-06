// LeetCode 68: Text Justification
// Explanation:
// 1. Greedy line building: pick as many words as possible until maxWidth.
// 2. If last line or single word, left-justify.
// 3. Otherwise, distribute spaces evenly across words.
// Time Complexity: O(n * L)
// Space Complexity: O(1)

class Solution {
public:
    vector<string> fullJustify(vector<string>& words, int maxWidth) {
        vector<string> res;
        int i = 0, n = words.size();
        while (i < n) {
            int lineLen = words[i].size();
            int j = i + 1;
            while (j < n && lineLen + words[j].size() + (j - i) <= maxWidth) {
                lineLen += words[j].size();
                j++;
            }
            int spaces = maxWidth - lineLen;
            int gaps = j - i - 1;
            string line;
            if (j == n || gaps == 0) {
                for (int k = i; k < j; k++) {
                    line += words[k];
                    if (k < j - 1) line += " ";
                }
                line += string(maxWidth - line.size(), ' ');
            } else {
                int space = spaces / gaps;
                int rem = spaces % gaps;
                for (int k = i; k < j - 1; k++) {
                    line += words[k];
                    line += string(space + (k - i < rem ? 1 : 0), ' ');
                }
                line += words[j - 1];
            }
            res.push_back(line);
            i = j;
        }
        return res;
    }
};

// Example usage:
// Solution sol;
// vector<string> words = {"This","is","an","example","of","text","justification."};
// auto res = sol.fullJustify(words, 16);
// for (auto &line : res) cout << '"' << line << '"' << endl;
