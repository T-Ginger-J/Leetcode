class Solution {
    fun multiply(num1: String, num2: String): String {
        if (num1 == "0" || num2 == "0") return "0"

        val m = num1.length
        val n = num2.length
        val res = IntArray(m + n)

        for (i in m - 1 downTo 0) {
            for (j in n - 1 downTo 0) {
                val mul = (num1[i] - '0') * (num2[j] - '0')
                val sum = mul + res[i + j + 1]

                res[i + j + 1] = sum % 10
                res[i + j] += sum / 10
            }
        }

        // Convert to string and remove leading zeros
        val sb = StringBuilder()
        for (digit in res) {
            if (!(sb.isEmpty() && digit == 0)) {
                sb.append(digit)
            }
        }

        return if (sb.isEmpty()) "0" else sb.toString()
    }
}

