<?php
class Solution {
    /**
     * @param Integer $num
     * @return String
     */
    function intToRoman($num) {
        $val = [1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1];
        $syms = ["M", "CM", "D", "CD",
                 "C", "XC", "L", "XL",
                 "X", "IX", "V", "IV",
                 "I"];

        $roman = "";

        for ($i = 0; $i < count($val); $i++) {
            while ($num >= $val[$i]) {
                $num -= $val[$i];
                $roman .= $syms[$i];
            }
        }

        return $roman;
    }
}
