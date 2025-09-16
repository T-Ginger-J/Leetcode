class Solution
  def spiral_order(matrix)
    res = []
    top, bottom = 0, matrix.length - 1
    left, right = 0, matrix[0].length - 1

    while top <= bottom && left <= right
      (left..right).each { |j| res << matrix[top][j] }
      top += 1

      (top..bottom).each { |i| res << matrix[i][right] }
      right -= 1

      if top <= bottom
        right.downto(left) { |j| res << matrix[bottom][j] }
        bottom -= 1
      end

      if left <= right
        bottom.downto(top) { |i| res << matrix[i][left] }
        left += 1
      end
    end

    res
  end
end

