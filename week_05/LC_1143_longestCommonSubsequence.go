func longestCommonSubsequence(text1 string, text2 string) int {
    n, m := len(text1), len(text2)
    memo := make([][]int, n)
    for i := range memo {
        memo[i] = make([]int, m)
        for j := range memo[i] {
            memo[i][j] = -1   // -1 表示没有计算过
        }
    }

    var dfs func(int, int) int
    dfs = func(i, j int) (res int) {
        if i < 0 || j < 0 {
            return
        }
        p := &memo[i][j]
        if *p != -1 {
            return *p
        }
        defer func() { *p = res } ()  // 记忆化
        if text1[i] == text2[j] {
            return dfs(i - 1, j - 1) + 1
        }
        return max(dfs(i - 1, j), dfs(i, j - 1))
    }
    return dfs(n - 1, m - 1)
}
