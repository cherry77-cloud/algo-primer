class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagram;
        for (auto &str : strs) {
            string sorted_str = str;
            ranges::sort(sorted_str);  // ranges::sort (C++20), 需要 #include <ranges> 或 <algorithm>
            anagram[sorted_str].emplace_back(str);
        }
        
        vector<vector<string>> ans;
        for (auto& [_, val] : anagram) {
            ans.emplace_back(std::move(val));
        }
        return ans;
    }
};
