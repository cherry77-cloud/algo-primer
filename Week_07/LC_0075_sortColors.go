func sortColors(nums []int)  {
    n := len(nums)
    ptr := 0
    for i := range nums {
        if nums[i] == 0 {
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
        }
    }
    for i := ptr; i < n; i++ {
        if nums[i] == 1 {
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
        }
    }
}
