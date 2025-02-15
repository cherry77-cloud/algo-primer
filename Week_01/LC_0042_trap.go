func trap(height []int) int {
    ans := 0
    n := len(height)
    preMax := make([]int, n)  // preMax[i] 表示从 height[0] 到 height[i] 的最大值
    preMax[0] = height[0]
    for i := 1; i < n; i++ {
        preMax[i] = max(preMax[i - 1], height[i])
    }

    sufMax := make([]int, n)
    sufMax[n - 1] = height[n - 1]  // sufMax[i] 表示从 height[i] 到 height[n-1] 的最大值
    for i := n - 2; i >= 0; i-- {
        sufMax[i] = max(sufMax[i + 1], height[i])
    }

    for i, h := range height {
        ans += min(preMax[i], sufMax[i]) - h  // 累加每个水桶能接多少水
    }

    return ans
}
