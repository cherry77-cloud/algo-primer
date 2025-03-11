func dailyTemperatures(temperatures []int) []int {
    // 栈中记录还没算出下一个更大元素的那些数的下标。相当于栈是一个 todolist
    // 在循环的过程中，现在还不知道答案是多少，在后面的循环中会算出答案。
    ans := make([]int, len(temperatures))
    st := []int{}   // todolist
    for i, t := range temperatures {
        for len(st) > 0 && t > temperatures[st[len(st)-1]] {
            j := st[len(st)-1]
            st = st[:len(st)-1]
            ans[j] = i - j
        }
        st = append(st, i)
    }
    return ans
}
