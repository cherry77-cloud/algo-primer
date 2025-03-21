```c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        ranges::sort(nums);
        vector<vector<int>> ans;
        int n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            int x = nums[i];
            if (i && nums[i - 1] == x)  continue;
            if (x + nums[i + 1] + nums[i + 2] > 0) break;
            if (x + nums[n - 2] + nums[n - 1] < 0) continue;
            int j = i + 1, k = n - 1;
            while (j < k) {
                int s = nums[j] + nums[k] + x;
                if (s < 0) j += 1;
                if (s > 0) k -= 1;
                if (s == 0) {
                    ans.push_back({x, nums[j], nums[k]});
                    j += 1;
                    while (j < k && nums[j] == nums[j - 1]) j++;
                    k -= 1;
                    while (k > j && nums[k] == nums[k + 1]) k--;
                }
            }
        }
        return ans;
    }
};
```

---
```go
func threeSum(nums []int) [][]int {
    ans := [][]int{}
    slices.Sort(nums)
    n := len(nums)
    for i, x := range nums[:n-2] {
        if i > 0 && x == nums[i - 1] {
            continue
        }
        if x + nums[i + 1] + nums[i + 2] > 0 {
            break
        }
        if x + nums[n - 2] + nums[n - 1] < 0 {
            continue
        }
        j, k := i + 1, n - 1
        for j < k {
            s := x + nums[j] + nums[k]
            if s > 0 {
                k -= 1
            } else if s < 0 {
                j += 1
            } else {
                ans = append(ans, []int{x, nums[j], nums[k]})
                for j++; j < k && nums[j] == nums[j - 1]; j++ {}
                for k--; k > j && nums[k] == nums[k + 1]; k-- {}
            }
        }
    }
    return ans
}
```
