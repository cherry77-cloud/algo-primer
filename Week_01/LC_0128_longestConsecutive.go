func longestConsecutive(nums []int) int {
    ans := 0
    has := map[int]bool{}
    for _, num := range nums {
        has[num] = true  // 把 nums 转换成哈希集合
    }

    for x := range has {  // 遍历哈希集合
        if has[x - 1] {
            continue
        }
        // x 是序列的起点
        y := x + 1
        for has[y] {  // 不断查找下一个数是否在哈希集合中
            y += 1
        }
        // 循环结束后, y-1 是最后一个在集合中的数
        ans = max(ans, y - x)
    }
    return ans
}
