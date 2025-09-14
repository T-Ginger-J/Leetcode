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

