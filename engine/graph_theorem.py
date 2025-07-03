from typing import List
from collections import defaultdict, deque


class GraphTheoremToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 207 · 课程表 ░░░░░░░░░░░░░░
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否可以完成所有课程（检测有向图是否有环）
            1. 构建邻接表和入度数组
            2. 将所有入度为 0 的节点加入队列
            3. 每次取出一个节点，将其所有后继节点的入度减 1
            4. 如果后继节点入度变为 0, 加入队列
            5. 最后检查是否所有节点都被处理（无环）
        """
        indegrees = [0 for _ in range(numCourses)]
        adjacency = defaultdict(list)
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegrees[cur] += 1
        queue = deque([u for u in range(numCourses) if indegrees[u] == 0])
        
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        
        return not numCourses

    # ░░░░░░░░░░░░░░ LeetCode 207 · 课程表 ░░░░░░░░░░░░░░
    @staticmethod
    def canFinish_dfs(numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        使用三色标记法检测有向图是否有环
            1. 白色: 未访问的节点
            2. 灰色: 正在访问的节点（在当前 DFS 路径上）
            3. 黑色: 已访问完成的节点（包括其所有子节点）
        核心思想
            - 如果在 DFS 过程中遇到灰色节点，说明形成了环
            - 因为灰色表示正在当前路径上，再次访问说明回到了起点
        """
        g = defaultdict(list)
        for cur, pre in prerequisites:
            g[pre].append(cur)
        WHITE = 0  # 白色: 未访问（未被垃圾回收器扫描）
        GRAY = 1   # 灰色: 正在访问（正在被垃圾回收器扫描，但子节点未完全扫描）
        BLACK = 2  # 黑色: 已访问完成（已被垃圾回收器完全扫描，包括所有子节点）
        colors = [WHITE] * numCourses
        
        def dfs(x: int) -> bool:
            colors[x] = GRAY                       # 标记为灰色，表示正在访问
            for y in g[x]:
                if colors[y] == GRAY:              # 遇到灰色节点，说明形成环
                    return True
                if colors[y] == WHITE and dfs(y):  # 白色节点继续DFS
                    return True
            colors[x] = BLACK                      # 标记为黑色，表示访问完成
            return False
        
        for i, c in enumerate(colors):
            if c == WHITE and dfs(i):
                return False
                
        return True

    # ░░░░░░░░░░░░░░ LeetCode 210 · 课程表 II ░░░░░░░░░░░░░░
    @staticmethod
    def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """返回完成所有课程的顺序（拓扑排序序列）。如果无法完成所有课程（有环），返回空数组"""
        g = defaultdict(list)
        indeg = [0] * numCourses
        for cur, pre in prerequisites:
            g[pre].append(cur)
            indeg[cur] += 1
        
        result: List[int] = []
        queue = deque([u for u in range(numCourses) if indeg[u] == 0])
        while queue:
            fa = queue.popleft()
            result.append(fa)
            for u in g[fa]:
                indeg[u] -= 1
                if indeg[u] == 0:
                    queue.append(u)
        
        return result if len(result) == numCourses else []
    
    # ░░░░░░░░░░░░░░ LeetCode 210 · 课程表 II ░░░░░░░░░░░░░░
    @staticmethod
    def findOrder_dfs(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """使用三色标记法返回逆拓扑序"""
        g = defaultdict(list)
        for cur, pre in prerequisites:
            g[pre].append(cur)
        
        WHITE, GRAY, BLACK = 0, 1, 2
        colors = [WHITE] * numCourses
        result: List[int] = []
        
        def dfs(x: int) -> bool:
            colors[x] = GRAY
            for y in g[x]:
                if colors[y] == GRAY:
                    return True
                if colors[y] == WHITE and dfs(y):
                    return True
            colors[x] = BLACK
            result.append(x)  # 在标记为黑色时加入结果
            return False
            
        for i, c in enumerate(colors):
            if colors[i] == WHITE and dfs(i):
                return []    # 有环，返回空列表
        
        return result[::-1]  # DFS 是深度优先，先访问的是依赖链的末端
