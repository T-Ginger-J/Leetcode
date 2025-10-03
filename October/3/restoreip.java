// LeetCode 93: Restore IP Addresses
// Explanation:
// 1. Use backtracking to try placing 3 dots, making 4 parts.
// 2. Each part must be valid (0-255, no leading zeros).
// 3. Collect valid IP addresses in result.
// Time Complexity: O(3^4) ≈ O(1)
// Space Complexity: O(1) excluding result

import java.util.*;

class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> res = new ArrayList<>();
        backtrack(s, 0, new ArrayList<>(), res);
        return res;
    }
    
    private void backtrack(String s, int start, List<String> path, List<String> res) {
        if (start == s.length() && path.size() == 4) {
            res.add(String.join(".", path));
            return;
        }
        if (path.size() >= 4) return;
        
        for (int len = 1; len <= 3 && start + len <= s.length(); len++) {
            String seg = s.substring(start, start+len);
            if ((seg.startsWith("0") && seg.length() > 1) || Integer.parseInt(seg) > 255) continue;
            path.add(seg);
            backtrack(s, start+len, path, res);
            path.remove(path.size()-1);
        }
    }
}
