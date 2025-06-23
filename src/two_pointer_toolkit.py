from typing import List
from collections import Counter, defaultdict


# =============================================================================
# 1.  Sliding Window
# =============================================================================
class SlidingWindowUtils:
    # ░░░░░░░░░░░ LeetCode 3 —— 无重复字符的最长子串 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """滑动窗口: 返回无重复字符的最长子串长度"""
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:           # 窗口内 c 出现次数 > 1，收缩左边界
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    # ░░░░░░░░░░░ LeetCode 438 —— 找到字符串中所有字母异位词 ░░░░░░░░░░░
    @staticmethod
    def findAnagrams(s: str, p: str) -> List[int]:
        """滑动窗口: 返回字符串 s 中所有 p 的字母异位词起始索引"""
        ans = []
        left = 0
        cnt = Counter(p)
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:           # 当前窗口 c 过多，收缩左边界
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        return ans
