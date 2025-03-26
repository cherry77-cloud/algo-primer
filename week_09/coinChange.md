```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        int n = coins.size();
        vector memo(n, vector<int>(amount + 1, -1));
        auto dfs = [&](this auto&&dfs, int i, int c) -> int {
            if (i < 0) {
                return c == 0 ? 0 : INT_MAX / 2;
            }
            int &res = memo[i][c];
            if (res != -1)  return res;
            if (c < coins[i]) {
                return res = dfs(i - 1, c);
            }
            return res = min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1);
        };
        int ans = dfs(n - 1, amount);
        return ans < INT_MAX / 2 ? ans : -1;
    }
};
```

---

```go
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
```
