from typing import List


class BinaryTemplate:
    """
    1. rightmost_red — 适用于 True ... True | False ... False 模式
       - 序列前半部分都是 True（红区），后半部分都是 False（蓝区）
       - 返回最后一个 True 的位置
    
    2. leftmost_blue — 适用于 False ... False | True ... True 模式
       - 序列前半部分都是 False（红区），后半部分都是 True（蓝区）
       - 返回第一个 True 的位置
    核心思想：任何满足"单调性"的布尔函数都可以使用
    """
    @staticmethod
    def rightmost_red(left: int, right: int, is_red: Callable[[int], bool]) -> int:
        """
        示例序列:  [T, T, T, T, F, F, F]
                            ↑
                        返回这个位置
        使用右中位数: (left + right + 1) // 2, 避免死循环
        case 1: mid 位置仍在红区, 更新 left = mid，保留 mid 作为候选答案
        case 2: mid 位置已经在蓝区, 更新 right = mid - 1，排除 mid
        """
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    @staticmethod
    def leftmost_blue(left: int, right: int, is_blue: Callable[[int], bool]) -> int:
        """
        示例序列:  [F, F, F, T, T, T, T]
                            ↑
                        返回这个位置
        # case 1: mid 位置已经在蓝区, 说明答案在 mid 或 mid 左边, 更新 right = mid，保留 mid 作为候选答案
        # case 2: mid 位置仍在红区, 说明答案一定在 mid 右边, 更新 left = mid + 1，排除 mid
        """
        while left < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid + 1
        return left

    @staticmethod
    def float_binary_search(
        left: float, 
        right: float, 
        check: Callable[[float], bool], 
        eps: float = 1e-9) -> float:
    """
    浮点数二分查找模板 - 寻找满足条件的最小值
    在连续区间 [left, right] 中找到满足 check(x) = True 的最小 x
    """
    while right - left > eps:
        mid = (left + right) / 2
        if check(mid):
            right = mid  # mid 满足条件，答案在 [left, mid]
        else:
            left = mid   # mid 不满足条件，答案在 [mid, right]
    return left  # 或 return right，差值小于 eps


class BinarySearchUtils:
    # ░░░░░░░░░░░░░░ LeetCode 34 —— 在排序数组中查找元素的第一个和最后一个位置 ░░░░░░░░░░░░░░
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ 使用两次二分：找最后一个红区元素 和 第一个蓝区元素 """
        def find_last_red(left: int = 0, right: int = len(nums) - 1) -> int:
            """ 找最后一个 <= target 的位置 """
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
        
        def find_first_blue(left: int = 0, right: int = len(nums) - 1) -> int:
            """ 找第一个 >= target 的位置 """
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        l1, l2 = find_last_red(0, len(nums) - 1), find_first_blue(0, len(nums) - 1)
        if not nums or nums[l1] != target:
            return [-1, -1]
        return [l2, l1]
        
    # ░░░░░░░░░░░ LeetCode 33 —— 搜索旋转排序数组 ░░░░░░░░░░░
    @staticmethod
    def search_rotated(nums: List[int], target: int) -> int:
        """
        红 / 蓝 区划分由下式给出
            is_red(i) = (x <= target) ^ (x > pivot) ^ (target > pivot), 其中 pivot = nums[-1]
        · 若 target 在右段：
            红区 = 左段全部 + 右段中 x <= target
            蓝区 = 右段中 x > target
        · 若 target 在左段：
            红区 = 左段中 x <= target
            蓝区 = 其余元素
        """
        left, right = 0, len(nums) - 1
        pivot = nums[-1]
        def is_red(i: int) -> bool:
            x = nums[i]
            return (x <= target) ^ (x > pivot) ^ (target > pivot)
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1: 红区→向右扩
                left = mid
            else:                        # case 2: 蓝区→向左收
                right = mid - 1
        return left if nums[left] == target else -1


class BinaryAnswerUtils:
    # ░░░░░░░░░░░ LeetCode 274 —— H 指数 ░░░░░░░░░░░
    @staticmethod
    def h_index(citations: List[int]) -> int:
        """
        二分答案：最大 h 使得“引用次数 ≥ h”的论文数 ≥ h
        红区: cnt ≥ h  —— 当前 h 可行，尝试更大  
        蓝区: cnt < h  —— 当前 h 不可行，调小
        """
        left, right = 0, max(citations)
        def is_red(h: int) -> bool:
            cnt = sum(cite >= h for cite in citations)
            return cnt >= h              # case 1：红区
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1：红区→向右扩
                left = mid
            else:                        # case 2：蓝区→向左收
                right = mid - 1
        return left
