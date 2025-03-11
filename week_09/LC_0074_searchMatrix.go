func searchMatrix(matrix [][]int, target int) bool {
    m, n := len(matrix), len(matrix[0])
    left, right := 0, m * n - 1
    for left < right {
        pivot := (left + right) / 2
        if matrix[pivot / n][pivot % n] >= target {
            right = pivot
        } else {
            left = pivot + 1
        }
    }
    return matrix[left / n][left % n] == target
}
