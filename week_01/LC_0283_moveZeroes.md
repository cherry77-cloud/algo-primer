## `C++`实现

```c++
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 0;
        while (right < n) {
            if (nums[right]) {
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};
```

---

## `go` 实现

```go
func moveZeroes(nums []int)  {
    left, right, n := 0, 0, len(nums)
    for right < n {
        if nums[right] != 0 {
            nums[right], nums[left] = nums[left], nums[right]
            left++
        }
        right++
    }
}
```
