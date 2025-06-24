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
