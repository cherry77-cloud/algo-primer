func numIslands(grid [][]byte) int {
    m, n := len(grid), len(grid[0])
    var dfs func(int, int)
    dfs = func(i, j int) {
        if i < 0 || i >= m || j < 0 || j >= n || grid[i][j] != '1' {
            return
        }
        grid[i][j] = '2'
        dfs(i, j + 1)
        dfs(i, j - 1)
        dfs(i - 1, j)
        dfs(i + 1, j)
    }

    ans := 0
    for i, row := range grid {
        for j, c := range row {
            if c == '1' {
                dfs(i, j)
                ans += 1
            }
        }
    }
    return ans
}
