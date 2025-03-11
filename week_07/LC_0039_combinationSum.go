func combinationSum(candidates []int, target int) [][]int {
    path := []int{}
    ans :=  [][]int{}
    var dfs func(int, int)
    dfs = func(i, left int) {
        if left == 0 {
            // 找到一个合法组合
            ans = append(ans, slices.Clone(path))
            return
        }

        if i == len(candidates) || left < 0 {
            return
        }

        // 不选
        dfs(i + 1, left)

        // 选
        path = append(path, candidates[i])
        dfs(i, left - candidates[i])
        path = path[:len(path) - 1]
    }
    dfs(0, target)
    return ans
}
