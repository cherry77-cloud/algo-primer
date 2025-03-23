```c++
class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        stack<int> st;
        for (int i = 0; i < height.size(); i++) {
            while (!st.empty() && height[i] >= height[st.top()]) {
                int bottom_h = height[st.top()];
                st.pop();
                if (st.empty()) break;
                int left = st.top();
                int dh = min(height[left], height[i]) - bottom_h;
                ans += dh * (i - left - 1);
            }
            st.push(i);
        }
        return ans;
    }
};
```

---

```go
func trap(height []int) int {
    ans := 0
    n := len(height)
    preMax := make([]int, n)  // preMax[i] 表示从 height[0] 到 height[i] 的最大值
    preMax[0] = height[0]
    for i := 1; i < n; i++ {
        preMax[i] = max(preMax[i - 1], height[i])
    }

    sufMax := make([]int, n)
    sufMax[n - 1] = height[n - 1]  // sufMax[i] 表示从 height[i] 到 height[n-1] 的最大值
    for i := n - 2; i >= 0; i-- {
        sufMax[i] = max(sufMax[i + 1], height[i])
    }

    for i, h := range height {
        ans += min(preMax[i], sufMax[i]) - h  // 累加每个水桶能接多少水
    }

    return ans
}
```
