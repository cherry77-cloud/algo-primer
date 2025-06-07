class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        unordered_set<int> seen(nums.begin(), nums.end());
        for (int x : seen) {
            if (seen.contains(x - 1)) {
                continue;
            }
            int y = x + 1;
            while (seen.contains(y)) {
                y += 1;
            }
            ans = max(ans, y - x);
        }
        return ans;
    }
};
