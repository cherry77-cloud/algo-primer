func productExceptSelf(nums []int) []int {
    n := len(nums)
    suf := make([]int, n)
    suf[n - 1] = 1
    for i := n - 2; i >= 0; i-- {
        suf[i] = suf[i + 1] * nums[i + 1]
    }

    pre := 1
    for i, x := range nums {
        // 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
        suf[i] *= pre
        pre *= x
    }

    return suf
}
