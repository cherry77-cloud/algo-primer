```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> parenthesis;
        string path;
        auto dfs = [&](this auto&& dfs, int u, int open) {
            if (u == 2 * n) {
                parenthesis.push_back(path);
                return;
            }
            if (open < n) {
                path.push_back('(');
                dfs(u + 1, open + 1);
                path.pop_back();
            }
            if (u - open < open) {
                path.push_back(')');
                dfs(u + 1, open);
                path.pop_back();
            }
        };

        dfs(0, 0);
        return parenthesis;
    }
};
```

---

```go
func generateParenthesis(n int) []string {
    m := n * 2
    ans := []string{}
    path := make([]byte, m)
    // i = 目前填了多少个括号
    // open = 左括号个数，i - open = 右括号个数
    var dfs func(int, int)

    dfs = func(i, open int) {
        if i == m {
            ans = append(ans, string(path))
            return
        }
        if open < n {         // 可以填左括号
            path[i] = '('
            dfs(i + 1, open + 1)
        }
        if i - open < open {  // 可以填右括号
            path[i] = ')'
            dfs(i + 1, open)
        }
    }
    dfs(0, 0)
    return ans
}
```
