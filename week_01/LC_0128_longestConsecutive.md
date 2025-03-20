```c++
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        unordered_set<int> has(nums.begin(), nums.end());
        for (int x : has) {
            if (has.contains(x - 1)) {
                continue;
            }
            int y = x + 1;
            while (has.contains(y)) {
                y += 1;
            }
            ans = max(ans, y - x);
        }
        return ans;
    }
};
```

---


```go
func longestConsecutive(nums []int) int {
    has := map[int]bool{}
    for _, num := range nums {
        has[num] = true
    }

    ans := 0
    for x := range has {
        if has[x - 1] {
            continue
        }
        y := x + 1
        for has[y] {
            y += 1
        }
        ans = max(ans, y - x)
    }
    return ans
}
```
