func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left < right {
        pivot := (left + right) / 2
        if nums[pivot] >= target {
            right = pivot
        } else {
            left = pivot + 1
        }
    }
    if nums[left] >= target {
        return left
    }
    return left + 1
}
