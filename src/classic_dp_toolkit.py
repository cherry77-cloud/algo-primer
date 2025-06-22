from collections import deque
from functools import cache
from math import inf, isqrt
from typing import List, Tuple

# ---------------------------------------------------------------------
# 1.  Grid‑style DP routines
# ---------------------------------------------------------------------
class GridToolkit:
    """Classic grid / matrix DP solved with memoised DFS (top‑down)."""

    # ░░░░░░░░░░░░░░ 120. Triangle minimum path sum ░░░░░░░░░░░░░░
    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        n = len(triangle)

        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:                # bottom row
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
            return (
                min(dfs(r - 1, c - 1), dfs(r - 1, c), dfs(r - 1, c + 1))
                + matrix[r][c]
            )

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
