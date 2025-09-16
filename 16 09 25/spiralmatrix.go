func spiralOrder(matrix [][]int) []int {
    if len(matrix) == 0 {
        return []int{}
    }

    res := []int{}
    top, bottom := 0, len(matrix)-1
    left, right := 0, len(matrix[0])-1

    for top <= bottom && left <= right {
        // left → right
        for j := left; j <= right; j++ {
            res = append(res, matrix[top][j])
        }
        top++

        // top → bottom
        for i := top; i <= bottom; i++ {
            res = append(res, matrix[i][right])
        }
        right--

        // right → left
        if top <= bottom {
            for j := right; j >= left; j-- {
                res = append(res, matrix[bottom][j])
            }
            bottom--
        }

        // bottom → top
        if left <= right {
            for i := bottom; i >= top; i-- {
                res = append(res, matrix[i][left])
            }
            left++
        }
    }

    return res
}

