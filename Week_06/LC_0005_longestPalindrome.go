func longestPalindrome(s string) string {
    start, end := 0, 0
    for i := 0; i < len(s); i++ {
        left1, right1 := expandAroundCenter(s, i, i)
        left2, right2 := expandAroundCenter(s, i, i + 1)
        if right1 - left1 > end - start {
            start, end = left1, right1
        }
        if right2 - left2 > end - start {
            start, end = left2, right2
        }
    }
    return s[start:end+1]
}

// 扩展法: 从中间开始，向外扩展寻找回文子串
func expandAroundCenter(s string, left int, right int) (int, int) {
    // 向外扩展，直到两侧字符不相等或越界
    for left >= 0 && right < len(s) && s[left] == s[right] {
        left--
        right++
    }
    return left + 1, right - 1
}
