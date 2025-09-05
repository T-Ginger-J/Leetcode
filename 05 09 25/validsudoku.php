<?php
class Solution {
    function solveSudoku(&$board) {
        $this->solve($board);
    }

    private function solve(&$board) {
        for ($i = 0; $i < 9; $i++) {
            for ($j = 0; $j < 9; $j++) {
                if ($board[$i][$j] === '.') {
                    for ($c = '1'; $c <= '9'; $c++) {
                        if ($this->isValid($board, $i, $j, $c)) {
                            $board[$i][$j] = $c;
                            if ($this->solve($board)) return true;
                            $board[$i][$j] = '.'; // backtrack
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    private function isValid($board, $row, $col, $c) {
        for ($i = 0; $i < 9; $i++) {
            if ($board[$row][$i] === $c || $board[$i][$col] === $c) return false;
            $boxRow = 3 * intdiv($row, 3) + intdiv($i, 3);
            $boxCol = 3 * intdiv($col, 3) + $i % 3;
            if ($board[$boxRow][$boxCol] === $c) return false;
        }
        return true;
    }
}

