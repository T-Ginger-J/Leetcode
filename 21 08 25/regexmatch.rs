use std::collections::HashMap;

impl Solution {
    pub fn is_matchDP(s: String, p: String) -> bool {
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

    pub fn is_match(s: String, p: String) -> bool {
        fn dfs(
            i: usize,
            j: usize,
            s: &Vec<char>,
            p: &Vec<char>,
            memo: &mut HashMap<(usize, usize), bool>,
        ) -> bool {
            if let Some(&ans) = memo.get(&(i, j)) {
                return ans;
            }

            // if pattern fully consumed, string must be too
            if j == p.len() {
                return i == s.len();
            }

            let first_match = i < s.len() && (s[i] == p[j] || p[j] == '.');

            let ans = if j + 1 < p.len() && p[j + 1] == '*' {
                // either skip x* or consume one char if it matches
                dfs(i, j + 2, s, p, memo) || (first_match && dfs(i + 1, j, s, p, memo))
            } else {
                first_match && dfs(i + 1, j + 1, s, p, memo)
            };

            memo.insert((i, j), ans);
            ans
        }

        let mut memo = HashMap::new();
        let s_chars: Vec<char> = s.chars().collect();
        let p_chars: Vec<char> = p.chars().collect();
        dfs(0, 0, &s_chars, &p_chars, &mut memo)
    }
}
