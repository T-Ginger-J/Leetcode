class Solution {
    func romanToInt(_ s: String) -> Int {
        let values: [Character: Int] = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        ]
        
        var total = 0
        var prev = 0
        
        for c in s.reversed() {
            let val = values[c]!
            if val < prev {
                total -= val
            } else {
                total += val
            }
            prev = val
        }
        
        return total
    }
}
