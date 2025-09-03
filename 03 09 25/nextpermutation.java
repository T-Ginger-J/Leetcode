import java.util.Arrays;

class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length - 2;

        // Step 1: Find first decreasing element from the end
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }

        if (i >= 0) {
            int j = nums.length - 1;
            // Step 2: Find element just larger than nums[i]
            while (nums[j] <= nums[i]) {
                j--;
            }
            swap(nums, i, j);
        }

        // Step 3: Reverse the tail
        reverse(nums, i + 1, nums.length - 1);
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }

    private void reverse(int[] nums, int left, int right) {
        while (left < right) {
            swap(nums, left, right);
            left++;
            right--;
        }
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] nums1 = {1,2,3};
        sol.nextPermutation(nums1);
        System.out.println(Arrays.toString(nums1)); // [1,3,2]

        int[] nums2 = {3,2,1};
        sol.nextPermutation(nums2);
        System.out.println(Arrays.toString(nums2)); // [1,2,3]

        int[] nums3 = {1,1,5};
        sol.nextPermutation(nums3);
        System.out.println(Arrays.toString(nums3)); // [1,5,1]
    }
}
