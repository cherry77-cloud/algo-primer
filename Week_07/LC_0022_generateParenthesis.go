func generateParenthesis(n int) []string {
    m := n * 2
    ans := []string{}
    path := make([]byte, m)
    // i = 目前填了多少个括号
    // open = 左括号个数，i - open = 右括号个数
    var dfs func(int, int)

    dfs = func(i, open int) {
        if i == m {
            ans = append(ans, string(path))
            return
        }
        if open < n {         // 可以填左括号
            path[i] = '('
            dfs(i + 1, open + 1)
        }
        if i - open < open {  // 可以填右括号
            path[i] = ')'
            dfs(i + 1, open)
        }
    }
    dfs(0, 0)
    return ans
}
