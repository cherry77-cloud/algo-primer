```cpp
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> ans;
        int cnt[26]{};
        for (char c : p)  cnt[c - 'a']++;

        int left = 0;
        for (int right = 0; right < s.length(); right++) {
            int  c = s[right] - 'a';
            cnt[c]--;
            while (cnt[c] < 0) {
                cnt[s[left] - 'a']++;
                left++;
            }
            if (right - left + 1 == p.length()) {
                ans.push_back(left);
            }
        }

        return ans;
    }
};
```

---

```go
func findAnagrams(s string, p string) []int {
    ans, cntP, cntS := []int{}, [26]int{}, [26]int{}
    for _, c := range p {  // 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
        cntP[c - 'a']++
    }
    for right, c := range s {
        cntS[c - 'a']++    // 右端点字母进入窗口
        left := right - len(p) + 1
        if left < 0 {      // 窗口长度不足 len(p)
            continue
        }
        if cntS == cntP {               // s' 和 p 的每种字母的出现次数都相同
            ans = append(ans, left)     // s' 左端点下标加入答案
        }
        cntS[s[left] - 'a']--           // 左端点字母离开窗口
    }
    return ans
}
```
