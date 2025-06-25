from typing import List


class BinarySearchUtils:
    # ░░░░░░░░░░░ LeetCode 704 —— 标准二分查找 ░░░░░░░░░░░
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

    # ░░░░░░░░░░░ LeetCode 33/81 —— 旋转升序数组查找 ░░░░░░░░░░░
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
