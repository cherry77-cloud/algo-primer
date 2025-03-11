func maxProduct(nums []int) int {
    ans := math.MinInt
    fMax, fMin := 1, 1
    for _, x := range nums {
        fMax, fMin = max(fMax * x, fMin * x, x), min(fMax * x, fMin * x, x)
        ans = max(fMax, ans)
    }
    return ans
}
