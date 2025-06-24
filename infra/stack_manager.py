from typing import List


class StackAlgoUtils:
    # ░░░░░░░░░░░ LeetCode 84 —— 柱状图中最大的矩形 ░░░░░░░░░░░
    @staticmethod
    def largest_rectangle_area(heights: List[int]) -> int:
        """返回柱状图中最大矩形的面积"""
        n = len(heights)
        left_bound: List[int] = [-1] * n    # 每个柱子左侧第一个更矮柱子的下标
        right_bound: List[int] = [n]  * n   # 每个柱子右侧第一个更矮柱子的下标
        stack: List[int] = []               # 自栈底 → 栈顶, 对应的柱子高度严格递增, 存下标

        # 遍历 heights，维护右边界，同时填充左边界
        for idx, height in enumerate(heights):
            # 处理出栈: 当前高度 ≤ 栈顶对应高度 ⇒ 栈顶柱子的右边界确定为 idx
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
