from typing import List


class MonotonicStackTemplates:
    # ░░░░░░░░░░░ 找每个元素右边第一个更大的元素 ░░░░░░░░░░░
    @staticmethod
    def next_greater_element(nums: List[int]) -> List[int]:
        """
        维护单调递减栈: 栈底 → 栈顶递减
            - 栈内存储还没找到答案的元素下标
            - 当遇到更大元素时，栈内元素依次出栈并记录答案
            - 当前元素就是这些出栈元素右边第一个更大的值
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认右边没有更大的元素
        stack = []         # 单调递减栈，存储还在等待答案的元素下标
        for i, num in enumerate(nums):
            # 当前元素比栈顶大 → 栈内元素找到了它们的答案, 就是当前元素
            while stack and num > nums[stack[-1]]:
                prev_idx = stack.pop()      # 弹出找到答案的元素
                result[prev_idx] = i        # 它的答案就是当前元素的位置
            stack.append(i)  # 当前元素入栈，等待找到它右边第一个更大的
        return result
    
    # ░░░░░░░░░░░ 找每个元素右边第一个更小的元素 ░░░░░░░░░░░
    @staticmethod
    def next_smaller_element(nums: List[int]) -> List[int]:
        """
        维护单调递增栈: 栈底 → 栈顶递增
            - 栈内存储还没找到答案的元素下标
            - 当遇到更小元素时，栈内元素依次出栈并记录答案
            - 当前元素就是这些出栈元素右边第一个更小的值
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认右边没有更小的元素
        stack = []         # 单调递增栈，存储还在等待答案的元素下标
        for i, num in enumerate(nums):
            # 当前元素比栈顶小 → 栈内元素找到了它们的答案（就是当前元素）
            while stack and num < nums[stack[-1]]:
                prev_idx = stack.pop()      # 弹出找到答案的元素
                result[prev_idx] = i        # 它的答案就是当前元素的位置
            stack.append(i)  # 当前元素入栈，等待找到它右边第一个更小的
        return result
    
    # ░░░░░░░░░░░ 找每个元素左边第一个更大的元素 ░░░░░░░░░░░
    @staticmethod
    def prev_greater_element(nums: List[int]) -> List[int]:
        """
        维护单调递减栈（栈底 → 栈顶递减）
            - 栈内存储可能成为后续元素答案的"候选者"
            - 弹出所有不可能成为答案的元素（≤当前元素的）
            - 栈顶元素就是当前元素左边第一个更大的
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认左边没有更大的元素
        stack = []         # 单调递减栈，存储可能成为答案的候选元素下标
        for i, num in enumerate(nums):
            # 弹出所有 ≤ 当前元素的栈顶, 它们不可能是后续元素的答案了
            while stack and num >= nums[stack[-1]]:
                stack.pop()  # 仅弹出，不记录
            # 经过弹出后，栈顶（如果存在）就是当前元素的答案
            if stack:
                result[i] = stack[-1]  # 当前元素的答案是栈顶
            stack.append(i)  # 当前元素入栈，可能成为后续元素的答案
        return result
    
    # ░░░░░░░░░░░ 找每个元素左边第一个更小的元素 ░░░░░░░░░░░
    @staticmethod
    def prev_smaller_element(nums: List[int]) -> List[int]:
        """
        维护单调递增栈: 栈底 → 栈顶递增
            - 栈内存储可能成为后续元素答案的"候选者"
            - 弹出所有不可能成为答案的元素（≥当前元素的）
            - 栈顶元素就是当前元素左边第一个更小的
        """
        n = len(nums)
        result = [-1] * n  # 初始化: 默认左边没有更小的元素
        stack = []         # 单调递增栈，存储可能成为答案的候选元素下标
        for i, num in enumerate(nums):
            # 弹出所有 ≥ 当前元素的栈顶, 它们不可能是后续元素的答案了
            while stack and num <= nums[stack[-1]]:
                stack.pop()  # 仅弹出，不记录
            # 经过弹出后，栈顶（如果存在）就是当前元素的答案
            if stack:
                result[i] = stack[-1]  # 当前元素的答案是栈顶
            stack.append(i)  # 当前元素入栈，可能成为后续元素的答案
        return result


class StackAlgoUtils:
    # ░░░░░░░░░░░ LeetCode 739 —— 每日温度 ░░░░░░░░░░░
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        """返回距离下一次更高温度的天数，若不存在则为 0"""
        n = len(temperatures)
        ans: List[int] = [0] * n
        stack: List[int] = []  # 下标栈，自底→顶温度递减
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        return ans

    # ░░░░░░░░░░░ LeetCode 84 —— 柱状图中最大的矩形 ░░░░░░░░░░░
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        """返回柱状图中最大矩形的面积"""
        n = len(heights)
        left_bound: List[int] = [-1] * n    # 每个柱子左侧第一个更矮柱子的下标
        right_bound: List[int] = [n]  * n   # 每个柱子右侧第一个更矮柱子的下标
        stack: List[int] = []               # 自栈底 → 栈顶, 对应的柱子高度严格递增, 存下标
        # 遍历 heights，维护右边界，同时填充左边界
        for idx, height in enumerate(heights):
            # 处理出栈: 当前高度 ≤ 栈顶对应高度 ⇒ 栈顶柱子的右边界确定为 idx
            # 当前高度 > 栈顶高度时，不淘汰（不出栈），直接将当前元素入栈
            while stack and height <= heights[stack[-1]]:
                prev_idx = stack.pop()
                right_bound[prev_idx] = idx
            if stack:     # 此时栈顶（若存在）就是 idx 的左侧第一个更矮柱子
                left_bound[idx] = stack[-1]
            stack.append(idx)

        max_area = 0
        for idx, height in enumerate(heights):
            width = right_bound[idx] - left_bound[idx] - 1
            max_area = max(max_area, height * width)
        return max_area

    # ░░░░░░░░░░░ LeetCode 85 —— 最大矩形 ░░░░░░░░░░░
    @staticmethod
    def maximalRectangle(matrix: List[List[str]]) -> int:
        """返回只包含 '1' 的最大矩形面积"""
        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            left, right, stack = [-1] * n, [n] * n, []
            for i, h in enumerate(heights):
                while stack and h < heights[stack[-1]]:
                    prev = stack.pop()
                    right[prev] = i
                if stack:
                    left[i] = stack[-1]
                stack.append(i)
            max_area = 0
            for h, l, r in zip(heights, left, right):
                max_area = max(max_area, (r - l - 1) * h)
            return max_area
        
        n_cols = len(matrix[0])
        heights: List[int] = [0] * n_cols
        max_area = 0
        for row in matrix:
            for j, val in enumerate(row):
                heights[j] = heights[j] + 1 if val == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))
        return max_area
