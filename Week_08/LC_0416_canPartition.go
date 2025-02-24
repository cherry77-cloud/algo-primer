func canPartition(nums []int) bool {
    n := len(nums)
    s := 0
    for _, x := range nums {
        s += x
    }
    if s % 2 != 0 {
        return false
    }
    memo := make([][]int, n)
    for i := range memo {
        memo[i] = make([]int, s / 2 + 1)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    }
    var dfs func(int, int) bool
    dfs = func(i, j int) bool {
        if i < 0 {
            return j == 0
        }
        p := &memo[i][j]
        if *p != -1 {
            return *p == 1
        }
        res := j >= nums[i] && dfs(i - 1, j - nums[i]) || dfs(i - 1, j)
        if res {
            *p = 1
        } else {
            *p = 0
        }
        return res
    }
    return dfs(n - 1, s / 2)
}
