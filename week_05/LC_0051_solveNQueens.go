func solveNQueens(n int) [][]string {
    ans := [][]string{}
    queens := make([]int, n)
    col := make([]bool, n)
    diag1 := make([]bool, n * 2 - 1)
    diag2 := make([]bool, n * 2 - 1)
    var dfs func(int)

    dfs = func(r int) {
        if r == n {
            board := make([]string, n)
            for i, c := range queens {
                board[i] = strings.Repeat(".", c) + "Q" + strings.Repeat(".", n - c - 1)
            }
            ans = append(ans, board)
            return
        }

        // 在 (r, c) 放皇后
        for c, ok := range col {
            rc := r - c + n - 1
            if !ok && !diag1[r+c] && !diag2[rc] {
                queens[r] = c
                col[c], diag1[r + c], diag2[rc] = true, true, true
                dfs(r + 1)
                col[c], diag1[r + c], diag2[rc] = false, false, false
            }
        }
    }

    dfs(0)
    return ans
}
