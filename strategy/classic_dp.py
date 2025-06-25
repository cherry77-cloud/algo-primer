from collections import deque
from functools import cache
from math import inf, isqrt
from typing import List, Tuple
from bisect import bisect_left


class KnapsackToolkit:
    # ░░░░░░░░░░░░░░ AcWing 2 —— 0-1 背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_01(volumes: List[int], values: List[int], capacity: int) -> int:
        """求最大价值；逆序容量的一维 0-1 DP"""
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ AcWing 3 —— 完全背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_complete(volumes: List[int], values: List[int], capacity: int) -> int:
        """求最大价值；顺序容量的一维完全背包 DP"""
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(vol, capacity + 1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ AcWing 8 —— 二维 0-1 背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_2d(volumes: List[int], weights: List[int],
                    values: List[int], max_volume: int, max_weight: int) -> int:
        """求最大价值；体积重量双维度倒序 0-1 DP"""
        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]
        for vol, wgt, val in zip(volumes, weights, values):
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)
        return dp[max_volume][max_weight]

    # ░░░░░░░░░░░░░░ AcWing 4 —— 多重背包（二进制拆分） ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_multiple_binary(volumes: List[int], values: List[int],
                                 counts: List[int], capacity: int) -> int:
        """求最大价值；二进制拆分转 0-1 背包"""
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

    # ░░░░░░░░░░░░░░ LeetCode 322 —— 零钱兑换 ░░░░░░░░░░░░░░
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        """求最少硬币数；完全背包 + 记忆化 DFS"""
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else inf
            not_take = dfs(i - 1, c)
            take = inf
            if c >= coins[i]:
                take = dfs(i, c - coins[i]) + 1
            return min(not_take, take)
        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

    # ░░░░░░░░░░░░░░ LeetCode 279 —— 完全平方数 ░░░░░░░░░░░░░░
    @staticmethod
    def numSquares(n: int) -> int:
        """求最少平方数数目；完全背包转移"""
        f = [0] + [inf] * n
        for i in range(1, isqrt(n) + 1):
            for j in range(i * i, n + 1):
                f[j] = min(f[j], f[j - i * i] + 1)
        return f[n]


class GridToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 120 —— 三角形最小路径和 ░░░░░░░░░░░░░░
    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        """自顶向下最小路径和；记忆化 DFS"""
        n = len(triangle)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0, 0)

    # ░░░░░░░░░░░░░░ LeetCode 64 —— 最小路径和 ░░░░░░░░░░░░░░
    @staticmethod
    def minPathSum(grid: List[List[int]]) -> int:
        """右下角最小路径和；记忆化 DFS"""
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return inf
            if i == 0 and j == 0:
                return grid[0][0]
            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ LeetCode 931 —— 下降路径最小和 ░░░░░░░░░░░░░░
    @staticmethod
    def minFallingPathSum(matrix: List[List[int]]) -> int:
        """任意起点下降路径最小和；三向转移 + 记忆化"""
        n = len(matrix)
        @cache
        def dfs(r: int, c: int) -> int:
            if c < 0 or c >= n:
                return inf
            if r == 0:
                return matrix[0][c]
            return min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1)) + matrix[r][c]
        return min(dfs(n - 1, col) for col in range(n))

    # ░░░░░░░░░░░░░░ LeetCode 62 —— 不同路径 ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePaths(m: int, n: int) -> int:
        """从左上到右下路径计数；组合数或 DFS"""
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ LeetCode 63 —— 不同路径 II ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        """含障碍路径计数；记忆化 DFS"""
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ LeetCode 329 —— 矩阵中的最长递增路径 ░░░░░░░░░░░░░░
    @staticmethod
    def longestIncreasingPath(matrix: List[List[int]]) -> int:
        """矩阵最长递增路径；四方向 DFS + 记忆化"""
        DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(i: int, j: int) -> int:
            best = 1
            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))
            return best
        return max(dfs(i, j) for i in range(m) for j in range(n))


class SubsequenceDPToolkit:
    # ░░░░░░░░░░░ LeetCode 300 —— 最长递增子序列 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        """LIS 长度；贪心 + 二分 tails"""
        tails: List[int] = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)

    # ░░░░░░░░░░░ LeetCode 1143 —— 最长公共子序列 ░░░░░░░░░░░
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        """LCS 长度；二维状态 DFS + 记忆化"""
        m, n = len(text1), len(text2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░ LeetCode 72 —— 编辑距离 ░░░░░░░░░░░
    @staticmethod
    def minDistance(word1: str, word2: str) -> int:
        """单词转换最少操作数；三向 DFS 记忆化"""
        m, n = len(word1), len(word2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
        return dfs(m - 1, n - 1)


class SubarrayDPToolkit:
    # ░░░░░░░░░░░ LeetCode 53 —— 最大子数组和 ░░░░░░░░░░░
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """连续子数组最大和；Kadane 一维 DP"""
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)
