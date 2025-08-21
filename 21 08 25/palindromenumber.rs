impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let s = x.to_string();
        s.chars().eq(s.chars().rev())
    }
    
    pub fn is_palindrome_stringless(x: i32) -> bool {
        // Negative numbers are not palindromes
        if x < 0 {
            return false;
        }
        // Numbers ending with 0 (but not 0 itself) are not palindromes
        if x % 10 == 0 && x != 0 {
            return false;
        }

        let mut x = x;
        let mut rev = 0;

        while x > rev {
            rev = rev * 10 + x % 10;
            x /= 10;
        }

        // For even length: x == rev
        // For odd length: x == rev / 10
        x == rev || x == rev / 10
    }


}
