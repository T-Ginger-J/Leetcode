#include <stdio.h>
#include <string.h>

char* intToRoman(int num, char* result) {
    int val[] = {1000, 900, 500, 400,
                 100, 90, 50, 40,
                 10, 9, 5, 4,
                 1};
    char* syms[] = {"M", "CM", "D", "CD",
                    "C", "XC", "L", "XL",
                    "X", "IX", "V", "IV",
                    "I"};

    result[0] = '\0';  // initialize result string

    for (int i = 0; i < 13; i++) {
        while (num >= val[i]) {
            num -= val[i];
            strcat(result, syms[i]);
        }
    }

    return result;
}