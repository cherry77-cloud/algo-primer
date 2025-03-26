```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        auto isPalindrome = [&](int left, int right) {
            while (left < right) {
                if (s[left++] != s[right--])  return false;
            }
            return true;
        };

        vector<vector<string>> ans;
        vector<string> path;

        auto dfs = [&](this auto&& dfs, int i) {  // 枚举起点
            if (i == s.length()) {
                ans.emplace_back(path);
                return;
            }

            for (int j = i; j < s.length(); j++) {   // 枚举终点  i->j
                if (isPalindrome(i, j)) {
                    path.push_back(s.substr(i, j - i + 1));
                    dfs(j + 1);
                    path.pop_back();
                }
            }
        };

        dfs(0);
        return ans;
    }
};
```

---

```go
func isPalindrome(s string, left, right int) bool {
    for left < right {
        if s[left] != s[right] {
            return false
        }
        left++
        right--
    }
    return true
}

func partition(s string) (ans [][]string) {
    n := len(s)
    path := []string{}

    var dfs func(int)
    dfs = func(i int) {
        if i == n {
            ans = append(ans, append([]string(nil), path...)) // 复制 path
            return
        }
        for j := i; j < n; j++ { // 枚举子串的结束位置
            if isPalindrome(s, i, j) {
                path = append(path, s[i:j+1])
                dfs(j + 1)
                path = path[:len(path)-1] // 恢复现场
            }
        }
    }

    dfs(0)
    return
}
```
