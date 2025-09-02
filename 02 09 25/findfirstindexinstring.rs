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

fn main() {
    println!("{}", Solution::str_str("hello".to_string(), "ll".to_string())); // 2
    println!("{}", Solution::str_str("aaaaa".to_string(), "bba".to_string())); // -1
}
