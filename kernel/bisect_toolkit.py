from typing import List


class BinaryTemplate:
    """
    1. rightmost_red — 适用于 True ... True | False ... False  单调序列，返回红区最后一个 True 的下标
    2. leftmost_blue — 适用于 False ... False | True ... True 单调序列， 返回蓝区第一个 True的下标
    任何满足下标方向只翻转一次的布尔函数，都可直接套用
    """
    @staticmethod
    def rightmost_red(left: int, right: int, is_red: Callable[[int], bool]) -> int:
        while left < right:
            mid = (left + right + 1) // 2      # 右中位，防死循环
            if is_red(mid):                    # case 1 · 仍在红区
                left = mid                     # 红区右扩
            else:                              # case 2 · 落入蓝区
                right = mid - 1                # 蓝区左缩
        return left

    @staticmethod
    def leftmost_blue(left: int, right: int, is_blue: Callable[[int], bool]) -> int:
        while left < right:
            mid = (left + right) // 2          # 左中位
            if is_blue(mid):                   # case 1 · 落入蓝区
                right = mid                    # 蓝区左扩
            else:                              # case 2 · 仍在红区
                left = mid + 1                 # 红区右移
        return left


class BinarySearchUtils:
    # ░░░░░░░░░░░ LeetCode 704 —— 二分查找 ░░░░░░░░░░░
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """
        红区: nums[mid] <= target —— mid 可能在目标左侧或就是目标  
        蓝区: nums[mid] > target  —— mid 一定在目标右侧
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:      # case 1：红区→向右扩
                left = mid
            else:                        # case 2：蓝区→向左收
                right = mid - 1
        return left if nums[left] == target else -1

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
