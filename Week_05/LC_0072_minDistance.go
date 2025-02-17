func minDistance(word1 string, word2 string) int {
    n, m := len(word1), len(word2)
    memo := make([][]int, n)
    for i := range memo {
        memo[i] = make([]int, m)
        for j := range memo[i] {
            memo[i][j] = -1
        }
    }

    var dfs func(int, int) int
    dfs = func(i, j int) (res int) {
        if i < 0 {
            return j + 1
        }
        if j < 0 {
            return i + 1
        }
        p := &memo[i][j]
        if *p != -1 {
            return *p
        }
        defer func() { *p = res } ()
        if word1[i] == word2[j] {
            return dfs(i - 1, j - 1)
        }
        return min(dfs(i - 1, j - 1), dfs(i, j - 1), dfs(i - 1, j)) + 1
    }
    return dfs(n - 1, m - 1)
}
