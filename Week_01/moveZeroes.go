func moveZeroes(nums []int)  {
    i0 := 0
    for i, x := range nums {
        if x != 0 {
            nums[i], nums[i0] = nums[i0], x
            i0 += 1
        }
    }
}
