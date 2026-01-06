//O(n)
class Solution {
    fun jump(nums: IntArray): Int {
        var jumps = 0
        var curEnd = 0
        var curFarthest = 0

        for (i in 0 until nums.size - 1) {
            curFarthest = maxOf(curFarthest, i + nums[i])
            if (i == curEnd) {
                jumps++
                curEnd = curFarthest
            }
        }

        return jumps
    }
}

fun main() {
    val sol = Solution()
    println(sol.jump(intArrayOf(2,3,1,1,4))) // 2
    println(sol.jump(intArrayOf(2,3,0,1,4))) // 2
}
