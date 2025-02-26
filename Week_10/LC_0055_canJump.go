func canJump(nums []int) bool {
    mx := 0
    for i, jump := range nums {
        if i > mx {              // 无法到达 i
            return false
        }
        mx = max(mx, i + jump)   // 从 i 最右可以跳到 i + jump
    }
    return true
}
