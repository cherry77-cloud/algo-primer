func coinChange(coins []int, amount int) int {
    f := make([]int, amount + 1)
    for i := range f {
        f[i] = math.MaxInt / 2
    }
    f[0] = 0
    for _, x := range coins {
        for c := x; c <= amount; c++ {
            f[c] = min(f[c], f[c - x] + 1)
        }
    }
    ans := f[amount]
    if ans < math.MaxInt / 2 {
        return ans
    }
    return -1
}
