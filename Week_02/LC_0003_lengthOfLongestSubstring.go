func lengthOfLongestSubstring(s string) int {
    ans := 0
    window := [128]bool{}
    left := 0
    for right, c := range s {
        // 如果窗口内已经包含 c，那么再加入一个 c 会导致窗口内有重复元素
        // 所以要在加入 c 之前，先移出窗口内的 c
        for window[c] {                      // 窗口内有 c
            window[s[left]] = false
            left += 1                        // 缩小窗口
        }
        window[c] = true                     // 加入 c
        ans = max(ans, right - left + 1)     // 更新窗口长度最大值
    }         
    return ans
}
