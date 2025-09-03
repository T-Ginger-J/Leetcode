struct Solution;

impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        const INT_MAX: i32 = 2_i32.pow(31) - 1;
        const INT_MIN: i32 = -2_i32.pow(31);

        if dividend == INT_MIN && divisor == -1 {
            return INT_MAX; // overflow
        }

        let negative = (dividend < 0) != (divisor < 0);

        let mut dividend = dividend.abs() as i64;
        let divisor = divisor.abs() as i64;
        let mut quotient: i64 = 0;

        while dividend >= divisor {
            let mut temp = divisor;
            let mut multiple = 1;
            while dividend >= (temp << 1) {
                temp <<= 1;
                multiple <<= 1;
            }
            dividend -= temp;
            quotient += multiple;
        }

        let result = if negative { -quotient } else { quotient };
        result as i32
    }
}

fn main() {
    println!("{}", Solution::divide(10, 3));       // 3
    println!("{}", Solution::divide(7, -3));       // -2
    println!("{}", Solution::divide(-2_i32.pow(31), -1)); // 2147483647
}
