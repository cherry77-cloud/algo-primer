from typing import List


class BinarySearchUtils:
    # ░░░░░░░░░░░ LeetCode 704 —— 二分查找 ░░░░░░░░░░░
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        """升序数组查找 target: 右中位"""
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        return left if nums[left] == target else -1


class BinaryAnswerUtils:
    # ░░░░░░░░░░░ LeetCode 274 —— H 指数 ░░░░░░░░░░░
    @staticmethod
    def h_index(citations: List[int]) -> int:
        """二分答案: 最大满足 cnt ≥ h 的 h"""
        left, right = 0, max(citations)

        def is_red(x: int) -> bool:
            cnt = sum(cite >= x for cite in citations)
            return cnt >= x

        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):
                left = mid
            else:
                right = mid - 1
        return left
