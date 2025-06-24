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

    # ░░░░░░░░░░░ LeetCode 438 · 找到字符串中所有字母异位词 ░░░░░░░░░░░
    @staticmethod
    def findAnagrams(s: str, p: str) -> List[int]:
       """滑动窗口: 返回字符串 s 中所有 p 的字母异位词起始索引"""
       ans = []
       left = 0
       cnt = Counter(p)                        # 初始化计数器: 需要哪些字符
       for right, c in enumerate(s):
           cnt[c] -= 1                         # 右边界扩展: 减少对字符c的需求
           while cnt[c] < 0:                   # 字符c多了，需要收缩左边界
               cnt[s[left]] += 1               # 移出左边字符，恢复需求
               left += 1                       # 左边界右移
           if right - left + 1 == len(p):
               ans.append(left)         
       return ans
    
    # ░░░░░░░░░░░ LeetCode 76 · 最小覆盖子串 ░░░░░░░░░░░
    @staticmethod
    def minWindow(s: str, t: str) -> str:
       ans_left, ans_right = -1, len(s)       # 记录最小窗口的边界
       cnt = defaultdict(int)
       for c in t:
           cnt[c] += 1                        # 统计t中每个字符的需求量
       
       less: int = len(cnt)                   # 还有几种字符没满足需求
       left: int = 0
       
       for right, c in enumerate(s):
           cnt[c] -= 1                         # 右边界扩展: 纳入字符c
           if cnt[c] == 0:                     # 字符 c 的需求刚好满足
               less -= 1
           
           while left <= right and less == 0:  # 所有字符都满足，尝试收缩
               if right - left < ans_right - ans_left:
                   ans_right, ans_left = right, left
               
               if cnt[s[left]] == 0:           # 即将移出的字符刚好够用
                   less += 1                   # 移出后将不满足需求
               cnt[s[left]] += 1               # 移出左边字符，增加需求
               left += 1
       return "" if ans_left < 0 else s[ans_left: ans_right + 1]


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

    # ░░░░░░░░░░░ LeetCode 15 —— 三数之和 ░░░░░░░░░░░
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans
