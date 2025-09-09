impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        fn backtrack(
            candidates: &Vec<i32>,
            target: i32,
            start: usize,
            path: &mut Vec<i32>,
            res: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                res.push(path.clone());
                return;
            }

            for i in start..candidates.len() {
                if candidates[i] <= target {
                    path.push(candidates[i]);
                    backtrack(candidates, target - candidates[i], i, path, res); // reuse same element
                    path.pop();
                }
            }
        }

        let mut res = vec![];
        let mut path = vec![];
        backtrack(&candidates, target, 0, &mut path, &mut res);
        res
    }
}

fn main() {
    let candidates = vec![2, 3, 6, 7];
    let target = 7;
    let res = Solution::combination_sum(candidates, target);

    for combo in res {
        println!("{:?}", combo);
    }
}
