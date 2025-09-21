class Solution {
    func permute(_ nums: [Int]) -> [[Int]] {
        var res = [[Int]]()
        
        func backtrack(_ path: [Int], _ remaining: [Int]) {
            if remaining.isEmpty {
                res.append(path)
                return
            }
            
            for i in 0..<remaining.count {
                var newPath = path
                newPath.append(remaining[i])
                var newRemaining = remaining
                newRemaining.remove(at: i)
                backtrack(newPath, newRemaining)
            }
        }
        
        backtrack([], nums)
        return res
    }
}

let sol = Solution()
print(sol.permute([1,2,3]))
// [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
