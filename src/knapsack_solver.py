from collections import deque
from typing import List, Tuple


class KnapsackToolkit:
  
    # --------------------------------------------------------
    #  0-1 背包  ——  AcWing 2
    # --------------------------------------------------------
    @staticmethod
    def knapsack_01(volumes: List[int], values: List[int], capacity: int) -> int:
        """
        0-1 背包 - AcWing 2
        功能：每件物品最多选一次，在容量 capacity 限制下获得最大价值
        """
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            # 体积 j 需倒序遍历，防止同一轮把同件物品选多次
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # --------------------------------------------------------
    #  完全背包 ——  AcWing 3
    # --------------------------------------------------------
    @staticmethod
    def knapsack_complete(volumes: List[int], values: List[int], capacity: int) -> int:
        """
        功能：每件物品可选任意次（无限件），在容量 capacity 内取得最大价值  
        关键：内层体积 j **正序** 遍历，允许当轮再次使用当前物品
        """
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(vol, capacity + 1):              # 正序，允许重复选
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # --------------------------------------------------------
    #  二维 0-1 背包  ——  AcWing 8
    # --------------------------------------------------------
    @staticmethod
    def knapsack_2d(volumes: List[int], weights: List[int], values: List[int], max_volume: int, max_weight: int) -> int:
        """
        二维费用背包（体积 + 重量）- 0-1 约束 · AcWing 8  
        功能：每件物品只能选一次，体积 ≤ max_volume 且重量 ≤ max_weight 时获得的最大价值
        """
        # dp[v][w] = 体积不超过 v，重量不超过 w 时的最大价值
        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]

        for vol, wgt, val in zip(volumes, weights, values):
            # 倒序遍历两维，确保同一件物品只选一次
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)
        return dp[max_volume][max_weight]

    # --------------------------------------------------------
    #  多重背包（Binary Split）——  AcWing 4
    # --------------------------------------------------------
    @staticmethod
    def knapsack_multiple(volumes: List[int], values: List[int], counts: List[int], capacity: int) -> int:
        """
        功能：每件物品最多有 counts[i] 件；在容量 capacity 内取得最大价值  
        思路：把数量 s 拆成 1,2,4,… 的二进制块，转化为若干 0-1 物品
        """
        # ---------- 二进制拆分 ----------
        items: List[Tuple[int, int]] = []
        for v, w, s in zip(volumes, values, counts):
            k = 1
            while k <= s:
                items.append((v * k, w * k))
                s -= k
                k <<= 1
            if s:
                items.append((v * s, w * s))

        # ---------- 0-1 背包 ----------
        dp = [0] * (capacity + 1)
        for vol, val in items:
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # --------------------------------------------------------
    #  多重背包 · 单调队列优化 —— AcWing 4 进阶
    # --------------------------------------------------------
    @staticmethod
    def knapsack_multiple(volumes: List[int], values: List[int], counts: List[int], capacity: int) -> int:
        """
        思路：把同一物品按体积 vol 的 同余下标 分组, j = k*vol + r，滑动窗口大小 = counts[i]  
            用单调队列把复杂度由 O(N·V·cnt) 降到 O(N·V)
        """
        dp = [0] * (capacity + 1)
        for vol, val, cnt in zip(volumes, values, counts):
            for r in range(vol):
                q: deque[Tuple[int, int]] = deque()      # (k, dp[j] - k*val)
                k, j = 0, r
                while j <= capacity:
                    cur_val = dp[j] - k * val
                    while q and q[-1][1] <= cur_val:
                        q.pop()
                    q.append((k, cur_val))
                    while q[0][0] < k - cnt:
                        q.popleft()
                    dp[j] = q[0][1] + k * val
                    k += 1
                    j += vol  
        return dp[capacity]
