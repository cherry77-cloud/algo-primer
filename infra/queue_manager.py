from collections import deque
from typing import Deque, List


class QueueAlgoUtils:
    # ░░░░░░░░░░░ LeetCode 239 —— 滑动窗口最大值 ░░░░░░░░░░░
    @staticmethod
    def max_sliding_window(nums: List[int], k: int) -> List[int]:
        """返回每个长度为 k 的滑动窗口中的最大值"""
        ans : List[int] = []
        mono_q : Deque[int] = deque()

        for i, x in enumerate(nums):
            while mono_q and nums[mono_q[-1]] <= x:  # 1. 右边入
                mono_q.pop()                         # 维护 q 的单调性
            mono_q.append(i)

            if mono_q[0] <= i - k:                   # 2. 左边出
                mono_q.popleft()                     # 队首已经离开窗口了
            
            if i >= k - 1:
                ans.append(nums[mono_q[0]])          # 由于队首到队尾单调递减，所以窗口最大值就在队首
        
        return ans
