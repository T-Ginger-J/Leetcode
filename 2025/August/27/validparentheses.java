import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            switch (c) {
                case '(':
                    stack.push(')');
                    break;
                case '{':
                    stack.push('}');
                    break;
                case '[':
                    stack.push(']');
                    break;
                default:
                    if (stack.isEmpty() || stack.pop() != c) {
                        return false;
                    }
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("()"));        // true
        System.out.println(sol.isValid("()[]{}"));    // true
        System.out.println(sol.isValid("(]"));        // false
        System.out.println(sol.isValid("([)]"));      // false
        System.out.println(sol.isValid("{[]}"));      // true
    }
}
