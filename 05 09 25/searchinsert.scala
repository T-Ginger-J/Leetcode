object Solution {
    def searchInsert(nums: Array[Int], target: Int): Int = {
        var left = 0
        var right = nums.length - 1

        while (left <= right) {
            val mid = left + (right - left) / 2
            if (nums(mid) == target) {
                return mid
            } else if (nums(mid) < target) {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        left
    }

    def main(args: Array[String]): Unit = {
        println(searchInsert(Array(1,3,5,6), 5))  // Output: 2
        println(searchInsert(Array(1,3,5,6), 2))  // Output: 1
        println(searchInsert(Array(1,3,5,6), 7))  // Output: 4
        println(searchInsert(Array(1,3,5,6), 0))  // Output: 0
    }
}
