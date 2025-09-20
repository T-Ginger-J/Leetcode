var solveSudoku = function(board) {
    const rowMask = new Array(9).fill(0);
    const colMask = new Array(9).fill(0);
    const boxMask = new Array(9).fill(0);
    const empties = [];

    const boxIndex = (r, c) => Math.floor(r / 3) * 3 + Math.floor(c / 3);

    // Initialize masks and empty positions
    for (let r = 0; r < 9; r++) {
        for (let c = 0; c < 9; c++) {
            if (board[r][c] === ".") {
                empties.push([r, c]);
            } else {
                const d = parseInt(board[r][c]);
                const bit = 1 << (d - 1);
                rowMask[r] |= bit;
                colMask[c] |= bit;
                boxMask[boxIndex(r, c)] |= bit;
            }
        }
    }

    function backtrack(idx) {
        if (idx === empties.length) return true;

        const [r, c] = empties[idx];
        const b = boxIndex(r, c);

        // Available digits
        let available = ~(rowMask[r] | colMask[c] | boxMask[b]) & 0x1FF;

        while (available) {
            const bit = available & -available; // lowest set bit
            const d = Math.clz32(bit) ^ 31;     // bit index (0-8)
            const num = d + 1;

            // Place digit
            board[r][c] = String(num);
            rowMask[r] |= bit;
            colMask[c] |= bit;
            boxMask[b] |= bit;

            if (backtrack(idx + 1)) return true;

            // Undo
            rowMask[r] ^= bit;
            colMask[c] ^= bit;
            boxMask[b] ^= bit;
            board[r][c] = ".";

            available &= available - 1; // remove lowest set bit
        }
        return false;
    }

    backtrack(0);
};
