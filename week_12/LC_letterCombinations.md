```cpp
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> combinations;
        if (digits.empty())  return combinations;

        unordered_map<char, string> phoneMap{
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        
        string path;
        auto dfs = [&](this auto&& dfs, int u) {
            if (u == digits.length()) {
                combinations.push_back(path);
                return;
            }
            for (char c : phoneMap[digits[u]]) {
                path.push_back(c);
                dfs(u + 1);
                path.pop_back();
            }
        };

        dfs(0);

        return combinations;
    }
};
```

---

```go
var mapping = [...]string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}

func letterCombinations(digits string) (ans []string) {
    n := len(digits)
    if n == 0 {
        return
    }
    path := make([]byte, n) // 注意 path 长度一开始就是 n，不是空列表
    var dfs func(int)
    dfs = func(i int) {
        if i == n {
            ans = append(ans, string(path))
            return
        }
        for _, c := range mapping[digits[i]-'0'] {
            path[i] = byte(c) // 直接覆盖
            dfs(i + 1)
        }
    }
    dfs(0)
    return
}
```
