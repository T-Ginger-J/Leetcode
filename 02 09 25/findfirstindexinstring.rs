struct Solution;

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        let n = haystack.len();
        let m = needle.len();
        if m == 0 { return 0; }
        if m > n { return -1; }

        for i in 0..=n - m {
            if &haystack[i..i + m] == needle {
                return i as i32;
            }
        }
        -1
    }

    pub fn str_str_built_in(haystack: String, needle: String) -> i32 {
        haystack.find(&needle).map(|i| i as i32).unwrap_or(-1)
    }

    pub fn str_strKMP(haystack: String, needle: String) -> i32 {
        if needle.is_empty() { return 0; }

        let h: Vec<char> = haystack.chars().collect();
        let n: Vec<char> = needle.chars().collect();
        let m = n.len();

        // Build LPS (Longest Prefix Suffix) array
        let mut lps = vec![0; m];
        let mut len = 0;
        for i in 1..m {
            while len > 0 && n[i] != n[len] {
                len = lps[len - 1];
            }
            if n[i] == n[len] {
                len += 1;
                lps[i] = len;
            }
        }

        // Search using KMP
        let mut j = 0;
        for i in 0..h.len() {
            while j > 0 && h[i] != n[j] {
                j = lps[j - 1];
            }
            if h[i] == n[j] {
                j += 1;
            }
            if j == m {
                return (i + 1 - m) as i32;
            }
        }

        -1
    }

}

fn main() {
    println!("{}", Solution::str_str("hello".to_string(), "ll".to_string())); // 2
    println!("{}", Solution::str_str("aaaaa".to_string(), "bba".to_string())); // -1
}
