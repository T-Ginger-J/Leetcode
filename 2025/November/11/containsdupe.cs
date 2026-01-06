// LeetCode 217: Contains Duplicate
// Explanation:
// 1. Use HashSet to store elements as we traverse.
// 2. If element exists, return true.
// 3. Else insert it.
// Time Complexity: O(n)
// Space Complexity: O(n)

using System.Collections.Generic;

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> seen = new HashSet<int>();
        foreach (int num in nums) {
            if (seen.Contains(num))
                return true;
            seen.Add(num);
        }
        return false;
    }
}

// Solution sol = new Solution();
// Console.WriteLine(sol.ContainsDuplicate(new int[]{1,2,3,1})); // True
// Console.WriteLine(sol.ContainsDuplicate(new int[]{1,2,3,4})); // False
// Console.WriteLine(sol.ContainsDuplicate(new int[]{1,1,1,3,3,4,3,2,4,2})); // True
