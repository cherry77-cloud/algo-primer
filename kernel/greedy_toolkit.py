class GreedyToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 56 —— 合并区间 ░░░░░░░░░░░░░░
    @staticmethod
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        """
        合并所有重叠的区间
             1. 先按照区间左端点排序
             2. 遍历每个区间：
                - 如果当前区间与结果集最后一个区间重叠，则合并
                - 否则直接加入结果集
             3. 两个区间 [a,b] 和 [c,d] 重叠的条件是：c <= b
        """
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
        ans = []
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 可以合并
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans

    # ░░░░░░░░░░░░░░ LeetCode 1353 —— 最多可以参加的会议数目 ░░░░░░░░░░░░░░
    @staticmethod
    def maxEvents(events: List[List[int]]) -> int:
        """
        最多可以参加的会议数目（每天只能参加一个会议）
             1. 贪心策略: 每天都参加当前可选会议中结束时间最早的会议
             2. 按天模拟，维护当天可以参加的会议
             3. 使用最小堆存储可参加会议的结束时间
             4. 每天的处理流程：
                - 加入当天开始的会议
                - 移除已过期的会议
                - 选择结束最早的会议参加
        """
        # 找出最大结束时间，决定模拟天数
        max_day = max(end for _, end in events)
        groups = defaultdict(list)
        for start, end in events:
            groups[start].append(end)
        
        min_heap = []  # 最小堆，保存当前可选会议的结束时间
        attended = 0   # 已参加会议数
        
        for day in range(1, max_day + 1):           # 模拟从第 1 天到 max_day
            for end_time in groups[day]:            # 加入当天开始的会议
                heappush(min_heap, end_time)
        
            while min_heap and min_heap[0] < day:   # 清除已经过期的会议
                heappop(min_heap)
            
            if min_heap:                            # 选择一个最早结束的会议参加
                heappop(min_heap)
                attended += 1
        
        return attended
