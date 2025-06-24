from typing import List
from collections import defaultdict, deque


class GraphToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 207 · 课程表 ░░░░░░░░░░░░░░
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否可以完成所有课程（检测有向图是否有环）。使用拓扑排序：通过 BFS 不断移除入度为 0 的节点
        """
        # 统计每个节点的入度
        indegrees = [0 for _ in range(numCourses)]
        # 构建邻接表
        adjacency = defaultdict(list)
        
        # 建图：pre -> cur 表示先修 pre 才能修 cur
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegrees[cur] += 1
        
        # 将所有入度为 0 的节点加入队列
        queue = deque([u for u in range(numCourses) if indegrees[u] == 0])
        
        # BFS 拓扑排序
        while queue:
            pre = queue.popleft()
            numCourses -= 1  # 已处理一个课程
            
            # 将邻接节点的入度减 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:  # 入度为 0，可以学习该课程
                    queue.append(cur)
        
        # 如果所有课程都被处理，说明无环
        return not numCourses
