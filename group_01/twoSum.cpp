```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hashtable;
        for (int i = 0; i < nums.size(); i++) {
            auto it = hashtable.find(target - nums[i]);
            if (it != hashtable.end()) {
                // it->first 是键, it->second 是值
                // (*it).second 等价于 it->second
                return {i, it->second}; 
            }
            hashtable[nums[i]] = i;
        }
        return {};
    }
};
```
