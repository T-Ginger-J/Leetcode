<?php
class Solution {
    function longestValidParentheses($s) {
        $stack = [-1];  // base index
        $max_len = 0;

        for ($i = 0; $i < strlen($s); $i++) {
            if ($s[$i] === '(') {
                array_push($stack, $i);
            } else {
                array_pop($stack);
                if (empty($stack)) {
                    array_push($stack, $i);
                } else {
                    $max_len = max($max_len, $i - end($stack));
                }
            }
        }

        return $max_len;
    }
}

// Example Usage
$sol = new Solution();
echo $sol->longestValidParentheses("(()") . "\n";       // Output: 2
echo $sol->longestValidParentheses(")()())") . "\n";    // Output: 4
echo $sol->longestValidParentheses("") . "\n";          // Output: 0
?>
