class Solution
  def solve_sudoku(board)
    solve(board)
  end

  private

  def solve(board)
    (0..8).each do |i|
      (0..8).each do |j|
        if board[i][j] == '.'
          ('1'..'9').each do |c|
            if is_valid?(board, i, j, c)
              board[i][j] = c
              return true if solve(board)
              board[i][j] = '.'  # backtrack
            end
          end
          return false
        end
      end
    end
    true
  end

  def is_valid?(board, row, col, c)
    (0..8).each do |i|
      return false if board[row][i] == c || board[i][col] == c
      box_row = 3 * (row / 3) + i / 3
      box_col = 3 * (col / 3) + i % 3
      return false if board[box_row][box_col] == c
    end
    true
  end
end
