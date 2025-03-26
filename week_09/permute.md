```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, bool> mp;
        vector<vector<int>> ans;
        vector<int> path;

        auto dfs = [&](this auto&& dfs, int u) {
            if (u == n) {
                ans.emplace_back(path);
                return;
            }
            for (auto num : nums) {
                if (!mp[num]) {
                    mp[num] = true;
                    path.push_back(num);
                    dfs(u + 1);
                    path.pop_back();
                    mp[num] = false;
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
```
