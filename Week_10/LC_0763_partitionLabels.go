func partitionLabels(s string) (ans []int) {
    last := [26]int{}
    for i, c := range s {
        last[c-'a'] = i // 每个字母最后出现的下标
    }

    start, end := 0, 0
    for i, c := range s {
        end = max(end, last[c-'a']) // 更新当前区间右端点的最大值
        if end == i { // 当前区间合并完毕
            ans = append(ans, end-start+1) // 区间长度加入答案
            start = i + 1 // 下一个区间的左端点
        }
    }
    return
}
