func permute(nums []int) (ans [][]int) {
    n := len(nums)
    path := make([]int, n)
    onPath := make([]bool, n)
    var dfs func(int)
    dfs = func(i int) {
        if i == n {
            ans = append(ans, append([]int(nil), path...))
            return
        }
        for j, on := range onPath {
            if !on {
                path[i] = nums[j]
                onPath[j] = true
                dfs(i + 1)
                onPath[j] = false
            }
        }
    }
    dfs(0)
    return
}
