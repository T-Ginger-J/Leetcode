// LeetCode 71: Simplify Path
// Explanation:
// 1. Split by "/".
// 2. Use stack for directories.
// 3. Skip "." and empty parts, pop for "..".
// 4. Build canonical path.
// Time Complexity: O(n)
// Space Complexity: O(n)

public class Solution {
    public string SimplifyPath(string path) {
        var stack = new Stack<string>();
        foreach (var part in path.Split('/')) {
            if (part == "" || part == ".") continue;
            if (part == "..") {
                if (stack.Count > 0) stack.Pop();
            } else {
                stack.Push(part);
            }
        }
        var arr = stack.ToArray();
        Array.Reverse(arr);
        return "/" + string.Join("/", arr);
    }
}

// Example usage:
// Solution sol = new Solution();
// Console.WriteLine(sol.SimplifyPath("/home/"));       // "/home"
// Console.WriteLine(sol.SimplifyPath("/../"));         // "/"
// Console.WriteLine(sol.SimplifyPath("/home//foo/"));  // "/home/foo"
