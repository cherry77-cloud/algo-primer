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


# =============================================================================
# 2.  Prefix-Suffix Two-Pointer
# =============================================================================
class PrefixSuffixTwoPointerUtils:
    # ░░░░░░░░░░░ LeetCode 42 —— 接雨水 ░░░░░░░░░░░
    @staticmethod
    def trap(height: List[int]) -> int:
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

    # ░░░░░░░░░░░ LeetCode 11 —— 盛最多水的容器 ░░░░░░░░░░░
    @staticmethod
    def maxArea(height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)
        return max_area
