class Solution
  def divide(dividend, divisor)
    int_max = 2**31 - 1
    int_min = -2**31

    # Handle overflow case
    return int_max if dividend == int_min && divisor == -1

    negative = (dividend < 0) != (divisor < 0)

    dividend = dividend.abs
    divisor = divisor.abs
    quotient = 0

    while dividend >= divisor
      temp = divisor
      multiple = 1
      while dividend >= (temp << 1)
        temp <<= 1
        multiple <<= 1
      end
      dividend -= temp
      quotient += multiple
    end

    negative ? -quotient : quotient
  end
end
