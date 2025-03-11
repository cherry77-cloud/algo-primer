func singleNumber(nums []int) int {
    ans := 0
    for _, x := range nums {
        ans ^= x
    }
    return ans
}
