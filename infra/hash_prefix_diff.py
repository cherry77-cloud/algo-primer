from collections import defaultdict
from typing import List, Dict


class HashTableUtils:
    # ░░░░░░░░░░░ LeetCode 49 —— 字母异位词分组 ░░░░░░░░░░░
    @staticmethod
    def group_anagrams(strs: List[str]) -> List[List[str]]:
        """分组字符串数组中的字母异位词"""
        hashtable: Dict[tuple, List[str]] = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            hashtable[key].append(s)
        return list(hashtable.values())

    # ░░░░░░░░░░░ LeetCode 128 —— 最长连续序列 ░░░░░░░░░░░
    @staticmethod
    def longest_consecutive(nums: List[int]) -> int:
        """返回数组中最长连续序列的长度"""
        seen = set(nums)
        longest = 0
        for x in seen:
            if x - 1 in seen:
                continue
            y = x
            while y in seen:
                y += 1
            longest = max(longest, y - x)
        return longest

    # ░░░░░░░░░░░ LeetCode 560 —— 和为 K 的子数组 ░░░░░░░░░░░
    @staticmethod
    def subarray_sum(nums: List[int], k: int) -> int:
        """返回数组中和为 k 的子数组个数"""
        cnt: Dict[int, int] = defaultdict(int)
        pre_s: int = 0
        ans: int = 0
        for x in nums:
            cnt[pre_s] += 1          # 记录当前前缀和出现次数
            pre_s += x
            ans += cnt[pre_s - k]    # 查找是否存在前缀和 pre_s - k
        return ans
