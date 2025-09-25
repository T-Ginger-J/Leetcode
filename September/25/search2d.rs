// LeetCode 74: Search a 2D Matrix
// Explanation:
// 1. Flatten matrix indices into 1D for binary search.
// 2. Convert mid index back into (row, col).
// Time Complexity: O(log(m*n))
// Space Complexity: O(1)

impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        let m = matrix.len();
        let n = matrix[0].len();
        let mut left = 0;
        let mut right = m * n - 1;

        while left <= right {
            let mid = (left + right) / 2;
            let val = matrix[mid / n][mid % n];
            if val == target {
                return true;
            } else if val < target {
                left = mid + 1;
            } else {
                if mid == 0 { break; }
                right = mid - 1;
            }
        }
        false
    }
}

