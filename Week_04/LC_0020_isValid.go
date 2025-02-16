func isValid(s string) bool {
    if len(s) % 2 != 0 {
        return false
    }
    mp := map[rune]rune{')': '(', ']': '[', '}': '{'}
    st := []rune{}
    for _, c := range s {
        if mp[c] == 0 {  // c 是左括号
            st = append(st, c)  // 入栈
        } else {  // c 是右括号
            if len(st) == 0 || st[len(st)-1] != mp[c] {
                return false  // 没有左括号，或者左括号类型不对
            }
            st = st[:len(st)-1]  // 出栈
        }
    }
    return len(st) == 0  // 所有左括号必须匹配完毕
}
