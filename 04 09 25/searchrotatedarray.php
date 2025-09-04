<?php
class Solution {
    function search($nums, $target) {
        $left = 0;
        $right = count($nums) - 1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] === $target) {
                return $mid;
            }

            // Left half is sorted
            if ($nums[$left] <= $nums[$mid]) {
                if ($nums[$left] <= $target && $target < $nums[$mid]) {
                    $right = $mid - 1;
                } else {
                    $left = $mid + 1;
                }
            } else { // Right half is sorted
                if ($nums[$mid] < $target && $target <= $nums[$right]) {
                    $left = $mid + 1;
                } else {
                    $right = $mid - 1;
                }
            }
        }

        return -1;
    }
}

