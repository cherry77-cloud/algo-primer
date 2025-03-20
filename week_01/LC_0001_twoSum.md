
```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); i++) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                return {i, it->second};
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};
```
---

```go
func twoSum(nums []int, target int) []int {
    hashtable := map[int]int{}
    for i, x := range nums {
        if j, ok := hashtable[target - x]; ok {
            return []int{i, j}
        }
        hashtable[x] = i
    }
    return nil
}
```
