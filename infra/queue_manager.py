from collections import deque
from typing import Deque, List, Tuple


class QueueAlgoUtils:
    # ░░░░░░░░░░░ LeetCode 239 —— 滑动窗口最大值 ░░░░░░░░░░░
    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        """
        单调队列: 返回每个长度为 k 的滑动窗口中的最大值
            1. 维护一个单调递减队列（存储索引）
            2. 队首始终是当前窗口的最大值
            3. 新元素入队时，移除队尾所有小于等于它的元素
            4. 队首元素超出窗口范围时出队
           
        单调队列特性:
            - 队列中的元素按值单调递减: 队首最大，队尾最小
            - 队首（左端）: 存储当前窗口最大值的索引
            - 队尾（右端）: 最近加入的元素
            - 保证了 O(1) 时间获取窗口最大值
        """
        ans: List[int] = []
        mono_q: Deque[int] = deque()

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
    def knapsack_multiple_queue(
        volumes: List[int],
        values: List[int],
        counts: List[int],
        capacity: int
    ) -> int:
        """
        单调队列优化多重背包: 求最大价值
            1. 多重背包的朴素 DP: O(n*capacity*count)
            2. 优化思路: 按体积同余分组，每组内用单调队列优化
            3. 状态转移: dp[j] = max(dp[j-k*vol] + k*val), k ∈ [0, cnt]
            4. 同余分组: j % vol = r 的位置为一组，组内转移
        """
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
