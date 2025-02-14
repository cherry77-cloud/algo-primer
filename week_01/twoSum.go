func twoSum(nums []int, target int) []int {
    idx := map[int]int{}  // 创建一个空的哈希表
    for j, x := range nums {  // 枚举 j
        // 在左边找 nums[i], 满足 nums[i] + x = target
        if i, ok := idx[target - x]; ok {
            return []int{i, j} // 返回两个数的下标
        }
        idx[x] = j;  // 保存 nums[j] 和 j
    }
    return nil
}
