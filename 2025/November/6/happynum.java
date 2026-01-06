// LeetCode 202: Happy Number
// Explanation:
// 1. Use HashSet to track seen numbers.
// 2. Repeatedly replace n with sum of squares of digits.
// 3. Stop if n == 1 (happy) or repeats (unhappy).
// Time Complexity: O(log n)
// Space Complexity: O(log n)

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while (n != 1 && !seen.contains(n)) {
            seen.add(n);
            int next = 0;
            while (n > 0) {
                int d = n % 10;
                next += d * d;
                n /= 10;
            }
            n = next;
        }
        return n == 1;
    }
}

/*
Solution sol = new Solution();
System.out.println(sol.isHappy(19)); // true
System.out.println(sol.isHappy(2));  // false

 */