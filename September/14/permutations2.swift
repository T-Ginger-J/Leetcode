class Solution {
    func permuteUnique(_ nums: [Int]) -> [[Int]] {
        var res = [[Int]]()
        let nums = nums.sorted()
        var used = [Bool](repeating: false, count: nums.count)
        
        func backtrack(_ path: [Int]) {
            if path.count == nums.count {
                res.append(path)
                return
            }
            for i in 0..<nums.count {
                if used[i] { continue }
                if i > 0 && nums[i] == nums[i-1] && !used[i-1] { continue }
                used[i] = true
                var newPath = path
                newPath.append(nums[i])
                backtrack(newPath)
                used[i] = false
            }
        }
        
        backtrack([])
        return res
    }
}

let sol = Solution()
print(sol.permuteUnique([1,1,2]))
// [[1,1,2],[1,2,1],[2,1,1]]
