func searchRange(nums []int, target int) []int {
    // Function to find the first occurrence of the target
    findFirstBlue := func(left, right int) int {
        for left < right {
            pivot := (left + right) / 2
            if nums[pivot] >= target {
                right = pivot
            } else {
                left = pivot + 1
            }
        }
        return left
    }

    // Function to find the last occurrence of the target
    findLastRed := func(left, right int) int {
        for left < right {
            pivot := (left + right + 1) / 2
            if nums[pivot] <= target {
                left = pivot
            } else {
                right = pivot - 1
            }
        }
        return left
    }

    l := findFirstBlue(0, len(nums)-1)
    r := findLastRed(0, len(nums)-1)
    if len(nums) > 0 && nums[l] == target {
        return []int{l, r}
    }
    return []int{-1, -1}
}
