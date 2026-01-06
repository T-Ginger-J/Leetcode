class Solution {
  int firstMissingPositive(List<int> nums) {
    int n = nums.length;

    for (int i = 0; i < n; i++) {
      while (nums[i] > 0 &&
             nums[i] <= n &&
             nums[nums[i] - 1] != nums[i]) {
        int temp = nums[nums[i] - 1];
        nums[nums[i] - 1] = nums[i];
        nums[i] = temp;
      }
    }

    for (int i = 0; i < n; i++) {
      if (nums[i] != i + 1) return i + 1;
    }

    return n + 1;
  }

  int firstMissingPositiveOneLine(List<int> nums) {
    final s = nums.toSet();
    return List.generate(nums.length + 1, (i) => i + 1)
               .firstWhere((x) => !s.contains(x));
  }

}

void main() {
  var sol = Solution();
  print(sol.firstMissingPositive([1,2,0]));       // 3
  print(sol.firstMissingPositive([3,4,-1,1]));    // 2
  print(sol.firstMissingPositive([7,8,9,11,12])); // 1


}
