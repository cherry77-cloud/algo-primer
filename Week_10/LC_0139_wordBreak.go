func wordBreak(s string, wordDict []string) bool {
    maxLen := 0
    words := make(map[string]bool, len(wordDict))
    for _, w := range wordDict {
        words[w] = true
        maxLen = max(maxLen, len(w))
    }

    n := len(s)
    f := make([]bool, n + 1)
    f[0] = true
    for i := 1; i <= n; i++ {
        for j := i - 1; j >= max(i - maxLen, 0); j-- {
            if f[j] && words[s[j:i]] {
                f[i] = true
                break
            }
        }
    }
    return f[n]
}
