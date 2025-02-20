func minPathSum(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    memo := make([][]int, m)
    for i := range memo {
        memo[i] = make([]int, n)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    }
    var dfs func(int, int) int
    dfs = func(i, j int) int {
        if i < 0 || j < 0 {
            return math.MaxInt
        }
        if i == 0 && j == 0 {
            return grid[i][j]
        }
        p := &memo[i][j]
        if *p == -1 {
            *p = min(dfs(i, j-1), dfs(i-1, j)) + grid[i][j]
        }
        return *p
    }
    return dfs(m - 1, n - 1)
}
