// LeetCode 67: Add Binary
// Explanation:
// 1. Traverse from right to left with carry.
// 2. Build result string and reverse it at the end.
// Time Complexity: O(max(len(a), len(b)))
// Space Complexity: O(max(len(a), len(b)))

public class Solution {
    public string AddBinary(string a, string b) {
        int i = a.Length - 1, j = b.Length - 1, carry = 0;
        var sb = new System.Text.StringBuilder();
        
        while (i >= 0 || j >= 0 || carry > 0) {
            int total = carry;
            if (i >= 0) total += a[i--] - '0';
            if (j >= 0) total += b[j--] - '0';
            sb.Insert(0, (total % 2).ToString());
            carry = total / 2;
        }
        return sb.ToString();
    }
}

// Example usage:
// Solution sol = new Solution();
// Console.WriteLine(sol.AddBinary("11", "1"));      // "100"
// Console.WriteLine(sol.AddBinary("1010", "1011")); // "10101"
