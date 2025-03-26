```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> f(n + 1, 0x3f3f3f3f);
        f[0] = 0;
        for (int i = 1; i * i <= n; i++) {
            int x = i * i;
            for (int j = x; j <= n; j++) {
                f[j] = min(f[j], f[j - x] + 1);
            }
        }
        return f[n];
    }
};
```

---

```go

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
```
