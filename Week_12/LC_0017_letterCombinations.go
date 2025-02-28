var mapping = [...]string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) (ans []string) {
    n := len(digits)
    if n == 0 {
        return
    }
    path := make([]byte, n) // 注意 path 长度一开始就是 n，不是空列表
    var dfs func(int)
    dfs = func(i int) {
        if i == n {
            ans = append(ans, string(path))
            return
        }
        for _, c := range mapping[digits[i]-'0'] {
            path[i] = byte(c) // 直接覆盖
            dfs(i + 1)
        }
    }
    dfs(0)
    return
}
