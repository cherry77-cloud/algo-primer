## `c++`实现
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

## 'go' 实现
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

---


## `python`实现
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        st = set(nums)  # 把 nums 转成哈希集合
        for x in st:  # 遍历哈希集合
            if x - 1 in st:
                continue
            # x 是序列的起点
            y = x + 1
            while y in st:  # 不断查找下一个数是否在哈希集合中
                y += 1
            # 循环结束后，y-1 是最后一个在哈希集合中的数
            ans = max(ans, y - x)  # 从 x 到 y-1 一共 y-x 个数
        return ans
```
