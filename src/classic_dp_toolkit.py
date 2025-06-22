from collections import deque
from functools import cache
from math import inf, isqrt
from typing import List, Tuple

# =============================================================================
# 1.  Knapsack‑family templates
# =============================================================================
class KnapsackToolkit:
    # ░░░░░░░░░░░░░░ 0‑1 背包 —— AcWing 2 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_01(volumes: List[int], values: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ 完全背包 —— AcWing 3 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_complete(volumes: List[int], values: List[int], capacity: int) -> int:
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(vol, capacity + 1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ 二维 0‑1 背包 —— AcWing 8 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_2d(volumes: List[int], weights: List[int], values: List[int], max_volume: int, max_weight: int) -> int:
        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]
        for vol, wgt, val in zip(volumes, weights, values):
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)
        return dp[max_volume][max_weight]

    # ░░░░░░░░░░░░░░ 多重背包（Binary Split）—— AcWing 4 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_multiple_binary(volumes: List[int], values: List[int], counts: List[int], capacity: int) -> int:
        items: List[Tuple[int, int]] = []
        for v, w, s in zip(volumes, values, counts):
            k = 1
            while k <= s:
                items.append((v * k, w * k))
                s -= k
                k <<= 1
            if s:
                items.append((v * s, w * s))
        dp = [0] * (capacity + 1)
        for vol, val in items:
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ 多重背包·单调队列优化 —— AcWing 4 进阶 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_multiple_queue(volumes: List[int], values: List[int], counts: List[int], capacity: int) -> int:
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

    # ░░░░░░░░░░░░░░ 零钱兑换（完全背包）—— LeetCode 322 ░░░░░░░░░░░░░░
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else float('inf')
            not_take = dfs(i - 1, c)
            take = float('inf')
            if c >= coins[i]:
                take = dfs(i, c - coins[i]) + 1
            return min(not_take, take)
        ans = dfs(len(coins) - 1, amount)
        return ans if ans < float('inf') else -1

    # ░░░░░░░░░░░░░░ 完全平方数（完全背包）—— LeetCode 279 ░░░░░░░░░░░░░░
    @staticmethod
    def numSquares(n: int) -> int:
        f = [0] + [float('inf')] * n
        for i in range(1, isqrt(n) + 1):
            for j in range(i * i, n + 1):
                f[j] = min(f[j], f[j - i * i] + 1)
        return f[n]


# =============================================================================
# 2.  Grid‑style DP routines
# =============================================================================
class GridToolkit:
    # ░░░░░░░░░░░░░░ 120. Triangle minimum path sum ░░░░░░░░░░░░░░
    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        n = len(triangle)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0, 0)

    # ░░░░░░░░░░░░░░  64. Minimum path sum ░░░░░░░░░░░░░░
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[0][0]
            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ 931. Minimum falling path sum ░░░░░░░░░░░░░░
    @staticmethod
    def minFallingPathSum(matrix: List[List[int]]) -> int:
        n = len(matrix)
        @cache
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:
                return inf
            if r == 0:
                return matrix[0][c]
            return min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
        return min(dfs(n - 1, col) for col in range(n))

    # ░░░░░░░░░░░░░░  62. Unique paths ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░  63. Unique paths with obstacles ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)
