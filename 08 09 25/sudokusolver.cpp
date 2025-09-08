class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        int rowMask[9] = {0}, colMask[9] = {0}, boxMask[9] = {0};
        vector<pair<int, int>> empties;

        auto boxIndex = [](int r, int c) { return (r / 3) * 3 + (c / 3); };

        // Initialize masks
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empties.push_back({r, c});
                } else {
                    int d = board[r][c] - '0';
                    int bit = 1 << (d - 1);
                    rowMask[r] |= bit;
                    colMask[c] |= bit;
                    boxMask[boxIndex(r, c)] |= bit;
                }
            }
        }

        function<bool(int)> backtrack = [&](int idx) {
            if (idx == (int)empties.size()) return true;

            int r = empties[idx].first, c = empties[idx].second;
            int b = boxIndex(r, c);

            // Available digits
            int available = ~(rowMask[r] | colMask[c] | boxMask[b]) & 0x1FF;

            while (available) {
                int bit = available & -available;       // lowest set bit
                int d = __builtin_ctz(bit) + 1;         // digit (1-9)
                board[r][c] = '0' + d;

                // Place digit
                rowMask[r] |= bit;
                colMask[c] |= bit;
                boxMask[b] |= bit;

                if (backtrack(idx + 1)) return true;

                // Undo
                rowMask[r] ^= bit;
                colMask[c] ^= bit;
                boxMask[b] ^= bit;
                board[r][c] = '.';

                available &= available - 1; // remove lowest set bit
            }
            return false;
        };

        backtrack(0);
    }
};
