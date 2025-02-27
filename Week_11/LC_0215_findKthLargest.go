func findKthLargest(nums []int, k int) int {
    n := len(nums)
    return quickselect(nums, 0, n-1, n-k+1)
}

func quickselect(nums []int, l, r, k int) int {
    if l == r {
        return nums[l]
    }
    partition := nums[l]
    i := l - 1
    j := r + 1
    for i < j {
        for i++; nums[i] < partition; i++ {}
        for j--; nums[j] > partition; j-- {}
        if i < j {
            nums[i], nums[j] = nums[j], nums[i]
        }
    }

    left_part_size := j - l + 1
    if k <= left_part_size {
        return quickselect(nums, l, j, k)
    } else {
        return quickselect(nums, j+1, r, k-left_part_size)
    }
}
