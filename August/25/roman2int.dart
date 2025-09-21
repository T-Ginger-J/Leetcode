class Solution {
  int romanToInt(String s) {
    final values = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    };
    
    int total = 0;
    int prev = 0;
    
    for (var i = s.length - 1; i >= 0; i--) {
      int v = values[s[i]]!;
      if (v < prev) {
        total -= v;
      } else {
        total += v;
      }
      prev = v;
    }
    
    return total;
  }
}
