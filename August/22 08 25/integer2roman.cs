using System;

public class Solution {
    public string IntToRoman(int num) {
        int[] val = {1000, 900, 500, 400,
                     100, 90, 50, 40,
                     10, 9, 5, 4,
                     1};
        string[] syms = {"M", "CM", "D", "CD",
                         "C", "XC", "L", "XL",
                         "X", "IX", "V", "IV",
                         "I"};

        System.Text.StringBuilder roman = new System.Text.StringBuilder();

        for (int i = 0; i < val.Length; i++) {
            while (num >= val[i]) {
                num -= val[i];
                roman.Append(syms[i]);
            }
        }

        return roman.ToString();
    }
}
