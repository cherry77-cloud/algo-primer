func climbStairs(n int) int {
    memo := make([]int, n + 1)
    var dfs func(int) int
    dfs = func(i int) int {
        if i <= 1 {
            return 1
        }
        p := &memo[i]
        if *p == 0 {
            *p = dfs(i - 1) + dfs(i - 2)
        }
        return *p
    }
    return dfs(n)
}
