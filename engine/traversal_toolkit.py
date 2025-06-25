from collections import deque
from typing import List, Deque, Tuple


class GridGraphSearch:
    # ░░░░░░░░░░░░░░░ LeetCode 200 —— 岛屿数量（Flood Fill） ░░░░░░░░░░░░░░░
    @staticmethod
    def num_islands_bfs(grid: List[List[str]]) -> int:
        """
        Flood Fill 算法: 统计网格图上的连通岛屿数量
            1. 遍历整个网格，找到每个未访问的陆地
            2. 从该陆地开始进行 Flood Fill（洪水填充）
            3. 将连通的所有陆地标记为已访问
            4. 每次 Flood Fill 代表发现一个新岛屿
        """
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

    # ░░░░░░░░░░░░░░░ LeetCode 994 —— 腐烂的橘子（BFS） ░░░░░░░░░░░░░░░
    @staticmethod
    def orangesRotting(grid: List[List[int]]) -> int:
        """
        多源 BFS: 计算所有橘子腐烂所需的最小分钟数
            1. 找出所有初始腐烂的橘子，作为 BFS 的多个起点
            2. 同时统计新鲜橘子的数量
            3. 每一轮 BFS 代表一分钟，所有腐烂橘子同时向四周传播
            4. 当没有新鲜橘子或无法继续传播时结束
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue: Deque[Tuple[int, int]] = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        minutes = 0
        while queue and fresh:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in (-1, 0), (0, -1), (1, 0), (0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            minutes += 1
        
        return -1 if fresh else minutes

    # ░░░░░░░░░░░░░░░ LeetCode 417 —— 太平洋大西洋水流问题（BFS/DFS） ░░░░░░░░░░░░░░░
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        多源 BFS/DFS: 寻找既可以流向太平洋又可以流向大西洋的单元格
            1. 正向思考: 从每个点出发看能否到达两个大洋（复杂）
            2. 逆向思考: 从海洋边界出发，看能到达哪些点（简单）
            3. 水往低处流，逆向则是往高处或等高处走
            4. 分别从太平洋和大西洋边界开始搜索
            5. 两次搜索结果的交集即为答案
        """
        m, n = len(heights), len(heights[0])
       
        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            queue = deque(starts)
            visited = set(starts)
            while queue:
                x, y = queue.popleft()
                for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
            return visited
           
        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            def dfs(x: int, y: int) -> None:
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited
           
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n - 1)] + [(i, n - 1) for i in range(m)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))
