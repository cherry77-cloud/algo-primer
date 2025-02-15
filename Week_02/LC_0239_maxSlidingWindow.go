func maxSlidingWindow(nums []int, k int) []int {
    ans := make([]int, 0, len(nums) - k + 1)
    q := []int{}
    for i, x := range nums {
        // 1. 入
        for len(q) > 0 && nums[q[len(q)-1]] <= x {
            q = q[:len(q) - 1]
        }
        q = append(q, i)    // 入队
        // 2. 出
        if i - q[0] >= k {  // 队首已经离开窗口
            q = q[1:]       // Go 的切片是 O(1)
        }
        // 3. 记录答案
        if i >= k - 1 {
            // 由于队首到队尾单调递减，所以窗口最大值就是队首
            ans = append(ans, nums[q[0]]) 
        }
    }
    return ans
}
