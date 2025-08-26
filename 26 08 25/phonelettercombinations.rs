struct Solution;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        if digits.is_empty() {
            return vec![];
        }

        let mapping = vec![
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        ];

        let mut result = Vec::new();
        let mut current = String::new();
        Self::backtrack(&digits, 0, &mapping, &mut current, &mut result);
        result
    }

    fn backtrack(
        digits: &str,
        index: usize,
        mapping: &Vec<&str>,
        current: &mut String,
        result: &mut Vec<String>,
    ) {
        if index == digits.len() {
            result.push(current.clone());
            return;
        }

        let digit = digits.as_bytes()[index] - b'0';
        let letters = mapping[digit as usize];

        for ch in letters.chars() {
            current.push(ch);
            Self::backtrack(digits, index + 1, mapping, current, result);
            current.pop(); // backtrack
        }
    }
}
