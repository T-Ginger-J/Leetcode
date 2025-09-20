const totalNQueens = n => {
  const solve = (r, cols, d1, d2) => {
    if (r === n) return 1;
    let count = 0, avail = ((1 << n) - 1) & ~(cols | d1 | d2);
    while (avail) {
      let bit = avail & -avail;
      avail -= bit;
      count += solve(r + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1);
    }
    return count;
  };
  return solve(0, 0, 0, 0);
};
