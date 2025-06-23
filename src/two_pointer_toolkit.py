from collections import defaultdict


# =============================================================================
# 1.  Sliding Window
# =============================================================================
class SlidingWindowUtils:
    # ░░░░░░░░░░░ LeetCode 3 —— 无重复字符的最长子串 ░░░░░░░░░░░
    def lengthOfLongestSubstring(self, s: str) -> int:
        """滑动窗口：返回无重复字符的最长子串长度"""
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:           # 窗口内 c 出现次数 > 1，收缩左边界
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
