

impl Solution {
    pub fn four_sum(mut nums: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let n = nums.len();
        let mut res = Vec::new();
        if n < 4 {
            return res;
        }

        nums.sort();

        for i in 0..n - 3 {
            if i > 0 && nums[i] == nums[i - 1] {
                continue; // skip duplicates
            }

            for j in i + 1..n - 2 {
                if j > i + 1 && nums[j] == nums[j - 1] {
                    continue; // skip duplicates
                }

                let new_target = target as i64 - nums[i] as i64 - nums[j] as i64;
                let mut left = j + 1;
                let mut right = n - 1;

                while left < right {
                    let sum = nums[left] as i64 + nums[right] as i64;
                    if sum == new_target {
                        res.push(vec![nums[i], nums[j], nums[left], nums[right]]);
                        left += 1;
                        right -= 1;

                        while left < right && nums[left] == nums[left - 1] {
                            left += 1;
                        }
                        while left < right && nums[right] == nums[right + 1] {
                            right -= 1;
                        }
                    } else if sum < new_target {
                        left += 1;
                    } else {
                        right -= 1;
                    }
                }
            }
        }

        res
    }
}
