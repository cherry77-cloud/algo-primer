func largestRectangleArea(heights []int) int {
    n := len(heights)
    left, right := make([]int, n), make([]int, n)
    for i := 0; i < n; i++ {
        right[i] = n
    }

    stack := []int{}
    for i := 0; i < n; i++ {
        for len(stack) > 0 && heights[stack[len(stack)-1]] >= heights[i] {
            right[stack[len(stack)-1]] = i
            stack = stack[:len(stack)-1]
        }
        if len(stack) > 0 {
            left[i] = stack[len(stack)-1]
        } else {
            left[i] = -1
        }
        stack = append(stack, i)
    }

    ans := 0
    for i := 0; i < n; i++ {
        ans = max(ans, (right[i] - left[i] - 1) * heights[i])
    }
    return ans
}
