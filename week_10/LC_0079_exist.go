var dirs = []struct{ x, y int }{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}

func exist(board [][]byte, word string) bool {
    m, n := len(board), len(board[0])
    var dfs func(int, int, int) bool
    dfs = func(i, j, k int) bool {
        if board[i][j] != word[k] { // 匹配失败
            return false
        }
        if k == len(word)-1 { // 匹配成功
            return true
        }
        board[i][j] = 0 // 标记访问过
        for _, d := range dirs {
            x, y := i+d.x, j+d.y // 相邻格子
            if 0 <= x && x < m && 0 <= y && y < n && dfs(x, y, k+1) {
                return true // 搜到了！
            }
        }
        board[i][j] = word[k] // 恢复现场
        return false // 没搜到
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if dfs(i, j, 0) {
                return true // 搜到了！
            }
        }
    }
    return false // 没搜到
}
