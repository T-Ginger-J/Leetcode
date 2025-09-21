<?php
//O(logn)
class Solution {
    function searchRange($nums, $target) {
        $first = $this->findBound($nums, $target, true);
        if ($first == -1) {
            return [-1, -1];
        }
        $last = $this->findBound($nums, $target, false);
        return [$first, $last];
    }

    private function findBound($nums, $target, $isFirst) {
        $left = 0;
        $right = count($nums) - 1;
        $bound = -1;

        while ($left <= $right) {
            $mid = intdiv($left + $right, 2);
            if ($nums[$mid] == $target) {
                $bound = $mid;
                if ($isFirst) {
                    $right = $mid - 1; // search left half
                } else {
                    $left = $mid + 1;  // search right half
                }
            } elseif ($nums[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid - 1;
            }
        }

        return $bound;
    }
}

// Example Usage
$sol = new Solution();
print_r($sol->searchRange([5,7,7,8,8,10], 8)); // Output: [3, 4]
print_r($sol->searchRange([5,7,7,8,8,10], 6)); // Output: [-1, -1]
?>
