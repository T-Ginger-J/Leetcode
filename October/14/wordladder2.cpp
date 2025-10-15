// LeetCode 126: Word Ladder II
// Explanation:
// 1. BFS to find shortest transformations.
// 2. DFS to reconstruct all paths.
// Time Complexity: O(n * L^2)
// Space Complexity: O(n * L)

#include <vector>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        unordered_map<string, vector<string>> parents;
        unordered_set<string> current, next;
        current.insert(beginWord);
        bool found = false;

        while (!current.empty() && !found) {
            for (auto &w : current) dict.erase(w);
            for (auto &w : current) {
                for (int i = 0; i < w.size(); i++) {
                    string t = w;
                    for (char c = 'a'; c <= 'z'; c++) {
                        t[i] = c;
                        if (dict.count(t)) {
                            next.insert(t);
                            parents[t].push_back(w);
                            if (t == endWord) found = true;
                        }
                    }
                }
            }
            swap(current, next);
            next.clear();
        }

        vector<vector<string>> res;
        vector<string> path = {endWord};
        function<void(string)> dfs = [&](string word) {
            if (word == beginWord) {
                reverse(path.begin(), path.end());
                res.push_back(path);
                reverse(path.begin(), path.end());
                return;
            }
            for (auto &p : parents[word]) {
                path.push_back(p);
                dfs(p);
                path.pop_back();
            }
        };
        if (found) dfs(endWord);
        return res;
    }
};
