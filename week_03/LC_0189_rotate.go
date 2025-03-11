func rotate(nums []int, k int)  {
    n := len(nums)
    k = k % n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
}

func reverse(nums []int, left, right int) {
    for left < right {
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    }
}
