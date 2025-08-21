impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let m = s.len();
        let n = p.len();
        let s: Vec<char> = s.chars().collect();
        let p: Vec<char> = p.chars().collect();

        let mut dp = vec![vec![false; n + 1]; m + 1];
        dp[0][0] = true;

        // handle patterns like a*, a*b*, etc. that can match empty string
        for j in (2..=n).step_by(2) {
            if p[j - 1] == '*' {
                dp[0][j] = dp[0][j - 2];
            }
        }

        for i in 1..=m {
            for j in 1..=n {
                if p[j - 1] != '*' {
                    dp[i][j] = dp[i - 1][j - 1]
                        && (s[i - 1] == p[j - 1] || p[j - 1] == '.');
                } else {
                    // zero occurrence
                    dp[i][j] = dp[i][j - 2];
                    // one or more occurrences
                    if s[i - 1] == p[j - 2] || p[j - 2] == '.' {
                        dp[i][j] = dp[i][j] || dp[i - 1][j];
                    }
                }
            }
        }

        dp[m][n]
    }
}
