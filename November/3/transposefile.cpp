// LeetCode 194: Transpose File (C++ Equivalent)
// Explanation:
// 1. Read file lines, split by space into matrix.
// 2. Transpose matrix and print.
// Time Complexity: O(n * m)
// Space Complexity: O(n * m)

#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<vector<string>> rows;
    string line;
    while (getline(cin, line)) {
        istringstream iss(line);
        vector<string> row;
        string word;
        while (iss >> word) row.push_back(word);
        rows.push_back(row);
    }

    int cols = rows[0].size();
    for (int i = 0; i < cols; ++i) {
        for (int j = 0; j < (int)rows.size(); ++j) {
            if (j > 0) cout << " ";
            cout << rows[j][i];
        }
        cout << endl;
    }
    return 0;
}
