func rob(nums []int) int {
    n := len(nums)
    memo := make([]int, n)
    for i := range memo {
        memo[i] = -1
    }
    var dfs func(int) int
    dfs = func(i int) int {
        if i < 0 {
            return 0
        }
        if memo[i] != -1 {
            return memo[i]
        }
        res := max(dfs(i - 1), dfs(i - 2) + nums[i])
        memo[i] = res
        return res
    }
    return dfs(n - 1)
}
