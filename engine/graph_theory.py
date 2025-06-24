from typing import List
from collections import defaultdict, deque


class GraphToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 207 · 课程表 ░░░░░░░░░░░░░░
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        判断是否可以完成所有课程（检测有向图是否有环）。使用拓扑排序：通过 BFS 不断移除入度为 0 的节点
        """
        indegrees = [0 for _ in range(numCourses)]
        adjacency = defaultdict(list)
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
            indegrees[cur] += 1
        queue = deque([u for u in range(numCourses) if indegrees[u] == 0])
        
        while queue:
            pre = queue.popleft()
            numCourses -= 1  # 已处理一个课程
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:  # 入度为 0，可以学习该课程
                    queue.append(cur)
        return not numCourses
