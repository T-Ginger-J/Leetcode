//O(n)
class Solution {
  int trap(List<int> height) {
    int left = 0, right = height.length - 1;
    int leftMax = 0, rightMax = 0;
    int res = 0;

    while (left < right) {
      if (height[left] < height[right]) {
        if (height[left] >= leftMax) {
          leftMax = height[left];
        } else {
          res += leftMax - height[left];
        }
        left++;
      } else {
        if (height[right] >= rightMax) {
          rightMax = height[right];
        } else {
          res += rightMax - height[right];
        }
        right--;
      }
    }

    return res;
  }

  int trapStack(List<int> h) {
    var stack = <int>[];
    int res = 0, i = 0;
    while (i < h.length) {
      while (stack.isNotEmpty && h[i] > h[stack.last]) {
        var top = stack.removeLast();
        if (stack.isEmpty) break;
        var distance = i - stack.last - 1;
        var boundedHeight = (h[i] < h[stack.last] ? h[i] : h[stack.last]) - h[top];
        res += distance * boundedHeight;
      }
      stack.add(i++);
    }
    return res;
  }

}

void main() {
  var sol = Solution();
  print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])); // 6
  print(sol.trap([4,2,0,3,2,5]));             // 9
}
