```cpp
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        ranges::sort(intervals);
        vector<vector<int>> ans;
        for (auto& p : intervals) {
            if (!ans.empty() && p[0] <= ans.back()[1]) {
                ans.back()[1] = max(ans.back()[1], p[1]);
            } else {
                ans.emplace_back(p);
            }
        }
        return ans;
    }
};
```

---

```go
func merge(intervals [][]int) [][]int {
    ans := [][]int{}
    slices.SortFunc(intervals, func(p, q []int) int { 
        return p[0] - q[0]
    })
    for _, p := range intervals {
        m := len(ans)
        if m > 0 && p[0] <= ans[m - 1][1] {            // 可以合并
            ans[m - 1][1] = max(ans[m - 1][1], p[1])   // 更新右端点最大值
        } else {                                       // 不相交，无法合并
            ans = append(ans, p)                       // 新的合并区间
        }
    }
    return ans
}
```
