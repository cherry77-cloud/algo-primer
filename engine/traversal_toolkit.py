from collections import deque
from typing import List, Deque, Tuple


class GridGraphSearch:
    # ░░░░░░░░░░░░░░░ LeetCode 200 —— 岛屿数量（Flood Fill） ░░░░░░░░░░░░░░░
    @staticmethod
    def num_islands_bfs(grid: List[List[str]]) -> int:
        """使用 Flood Fill 算法在网格图上统计连通岛屿数量"""
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        islands = 0

        def bfs(si: int, sj: int) -> None:
            queue: Deque[Tuple[int, int]] = deque([(si, sj)])
            grid[si][sj] = '0'
            while queue:
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        queue.append((nx, ny))
                      
        def dfs(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                dfs(i + dx, j + dy)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    bfs(i, j)
        return islands
