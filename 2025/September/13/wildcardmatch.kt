class Solution {
    fun isMatch(s: String, p: String): Boolean {
        var i = 0  // pointer for s
        var j = 0  // pointer for p
        var starIdx = -1
        var match = 0

        while (i < s.length) {
            if (j < p.length && (p[j] == s[i] || p[j] == '?')) {
                i++
                j++
            } else if (j < p.length && p[j] == '*') {
                starIdx = j
                match = i
                j++
            } else if (starIdx != -1) {
                j = starIdx + 1
                match++
                i = match
            } else {
                return false
            }
        }

        while (j < p.length && p[j] == '*') {
            j++
        }

        return j == p.length
    }

    fun main() {
    val sol = Solution()
    println(sol.isMatch("aa", "a"))        // false
    println(sol.isMatch("aa", "*"))        // true
    println(sol.isMatch("cb", "?a"))       // false
    println(sol.isMatch("adceb", "*a*b"))  // true
    println(sol.isMatch("acdcb", "a*c?b")) // false
}

}
