impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let val = [1000, 900, 500, 400,
                   100, 90, 50, 40,
                   10, 9, 5, 4,
                   1];
        let syms = ["M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV",
                    "I"];

        let mut roman = String::new();

        for i in 0..val.len() {
            while num >= val[i] {
                num -= val[i];
                roman.push_str(syms[i]);
            }
        }

        roman
    }
}
