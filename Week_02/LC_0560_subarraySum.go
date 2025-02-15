func subarraySum(nums []int, k int) int {
    ans, s := 0, 0
    cnt := map[int]int{0: 1}  // s[0] = 0 单独统计
    for _, x := range nums {
        s += x
        ans += cnt[s - k]
        cnt[s] += 1
    }
    return ans
}
