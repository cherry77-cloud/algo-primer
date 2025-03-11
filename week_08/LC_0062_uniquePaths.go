func uniquePaths(m int, n int) int {
    memo := make([][]int, m)
    for i := range memo {
        memo[i] = make([]int, n)
    }
    var dfs func(int, int) int
    dfs = func(i, j int) int {
        if i < 0 || j < 0 {
            return 0
        }
        if i == 0 && j == 0 {
            return 1
        }
        p := &memo[i][j]
        if *p == 0 {
            *p = dfs(i - 1, j) + dfs(i, j - 1)
        }
        return *p
    }
    return dfs(m - 1, n - 1)
}
