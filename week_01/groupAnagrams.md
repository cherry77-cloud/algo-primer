```c++
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> m;
        for (string &s : strs) {
            string sorted_s = s;
            ranges::sort(sorted_s);
            m[sorted_s].push_back(s);
        }

        vector<vector<string>> ans;
        for (auto& [_, val] : m) {
            ans.push_back(val);
        }

        return ans;
    }
};
```

---


```go
func groupAnagrams(strs []string) [][]string {
    m := map[string][]string{}
    for _, s := range strs {
        t := []byte(s)
        slices.Sort(t)
        sortedS := string(t)
        m[sortedS] = append(m[sortedS], s)
    }
    return slices.Collect(maps.Values(m))
}
```
