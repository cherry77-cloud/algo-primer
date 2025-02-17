func lengthOfLIS(nums []int) int {
    g := []int{}
    // 定义 g[i] 表示长为 i+1 的上升子序列的末尾元素的最小值
    for _, x := range nums {
        j := sort.SearchInts(g, x)
        if j == len(g) {   // >=x 的 g[j] 不存在
            g = append(g, x)
        } else {
            g[j] = x  
        }
    }
    return len(g)
}
