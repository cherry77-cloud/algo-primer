func subsets(nums []int) [][]int {
    ans := make([][]int, 1 << len(nums))
    for i := range ans {
        for j, x := range nums {    // 枚举全集 U 的所有子集 i
            if i >> j & 1 == 1 {
                ans[i] = append(ans[i], x)  // j 在集合 i 中
            }
        }
    }
    return ans
}
