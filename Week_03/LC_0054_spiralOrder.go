var dirs = [4][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func spiralOrder(matrix [][]int) []int {
    m, n := len(matrix), len(matrix[0])
    ans := make([]int, m * n)
    i, j, di := 0, 0, 0
    for k := range ans {              // 一共走 mn 步
        ans[k] = matrix[i][j]
        matrix[i][j] = math.MaxInt    // 标记，表示已经访问过（已经加入答案）
        x, y := i + dirs[di][0], j + dirs[di][1]   // 下一步的位置
        // 如果 (x, y) 出界或者已经访问过
        if x < 0 || x >= m || y < 0 || y >= n || matrix[x][y] == math.MaxInt {
            di = (di + 1) % 4    // 右转 90°
        }
        i += dirs[di][0]
        j += dirs[di][1]   // 走一步
    }
    return ans
}
