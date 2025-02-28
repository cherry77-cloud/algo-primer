func search(nums []int, target int) int {
    end := nums[len(nums) - 1]
    check := func(i int) bool {
        x := nums[i]
        if x > end {
            return target > end && x >= target
        }
        return target > end || x >= target
    }

    left, right := 0, len(nums) - 1
    for left < right {
        mid := (left + right) / 2
        if check(mid) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    if nums[left] != target {
        return -1
    }
    return left
}
