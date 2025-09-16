impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut max_sum = nums[0];
        let mut curr = 0;

        for n in nums {
            curr = curr.max(0) + n;      // start new subarray or extend
            max_sum = max_sum.max(curr);
        }

        max_sum
    }
}
