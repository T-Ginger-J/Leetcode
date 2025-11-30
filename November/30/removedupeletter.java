// LeetCode 316: Remove Duplicate Letters
// Explanation:
// 1. Stack-based greedy solution
// 2. Remove larger letters that appear later
// Time Complexity: O(n)
// Space Complexity: O(26)

import java.util.*;

class Solution {
    public String removeDuplicateLetters(String s) {
        int[] count = new int[26];
        boolean[] seen = new boolean[26];
        for(char c : s.toCharArray()) count[c - 'a']++;
        Stack<Character> stack = new Stack<>();
        for(char c : s.toCharArray()){
            count[c - 'a']--;
            if(seen[c - 'a']) continue;
            while(!stack.isEmpty() && c < stack.peek() && count[stack.peek() - 'a'] > 0){
                seen[stack.pop() - 'a'] = false;
            }
            stack.push(c);
            seen[c - 'a'] = true;
        }
        StringBuilder sb = new StringBuilder();
        for(char c : stack) sb.append(c);
        return sb.toString();
    }
}

