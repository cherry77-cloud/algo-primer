const N = 10000

func numSquares(n int) int {
    f := make([]int, N + 1)
    for i := 1; i <= N; i++ {
        f[i] = math.MaxInt
    }
    for i := 1; i * i <= n; i++ {
        for j := i * i; j <= N; j++ {
            f[j] = min(f[j], f[j - i * i] + 1)
        }
    }
    return f[n]
}
