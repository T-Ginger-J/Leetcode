function totalNQueens(n: number): number {
    function solve(r: number, cols: number, d1: number, d2: number): number {
        if (r === n) return 1;
        let count = 0;
        let avail = ((1 << n) - 1) & ~(cols | d1 | d2);
        while (avail) {
            const bit = avail & -avail;
            avail -= bit;
            count += solve(r + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1);
        }
        return count;
    }
    return solve(0, 0, 0, 0);
}
