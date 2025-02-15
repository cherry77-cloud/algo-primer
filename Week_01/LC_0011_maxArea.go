func maxArea(height []int) int {
    ans := 0
    left, right := 0, len(height) - 1
    for left < right {
        // (right - left) 是矩形的宽度，min(height[left], height[right]) 是矩形的高度
        area := (right - left) * min(height[left], height[right])
        ans = max(ans, area)
        // 使用双指针法，计算不同区间的水面积，并逐步移动指针寻找最大值。
        if height[left] < height[right] {
            left += 1
        } else {
            right -= 1
        }
    }
    return ans
}
