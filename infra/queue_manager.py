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
            while mono_q and nums[mono_q[-1]] <= x:
                mono_q.pop()
            mono_q.append(i)
            if mono_q[0] <= i - k:
                mono_q.popleft()
            if i >= k - 1:
                ans.append(nums[mono_q[0]])
        return ans

    # ░░░░░░░░░░░░░░ AcWing 4 进阶 —— 多重背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_multiple_queue(volumes: List[int], values: List[int],
                                counts: List[int], capacity: int) -> int:
        """求最大价值；同余分组 + 单调队列优化"""
        dp = [0] * (capacity + 1)
        for vol, val, cnt in zip(volumes, values, counts):
            for r in range(vol):
                q: deque[Tuple[int, int]] = deque()
                k = 0
                for j in range(r, capacity + 1, vol):
                    cur_val = dp[j] - k * val
                    while q and q[-1][1] <= cur_val:
                        q.pop()
                    q.append((k, cur_val))
                    while q[0][0] < k - cnt:
                        q.popleft()
                    dp[j] = q[0][1] + k * val
                    k += 1
        return dp[capacity]
