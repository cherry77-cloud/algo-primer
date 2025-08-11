class GreedyToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 1005 —— K 次取反后最大和 ░░░░░░░░░░░░░░
    @staticmethod
    def largestSumAfterKNegations(nums: List[int], k: int) -> int:
        """
        贪心策略：
             1. 先对数组排序（从小到大）
             2. 从左到右把负数尽量翻成正数，直到用完 k 或没有负数
             3. 计算总和；若 k 仍为奇数，则再对“绝对值最小”的元素取反一次
        说明：保持与你给出的实现一致，不改动核心代码/变量命名
        """
        nums.sort()
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
    
        total = sum(nums)
        min_abs = min(nums, key=abs)
        if k % 2 == 1:
            total -= 2 * min_abs
        return total
        
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

    # ░░░░░░░░░░░░░░ LeetCode 1353 —— 最多可以参加的会议数目（并查集解法） ░░░░░░░░░░░░░░
    @staticmethod
    def maxEvents_UnionFind(events: List[List[int]]) -> int:
        """
        最多可以参加的会议数目（并查集优化）
             1. 贪心策略：按结束时间排序，每个会议分配最早的可用天
             2. 并查集优化：fa[i] 指向第 i 天及之后的第一个空闲天
             3. 对每个会议 [start, end]：
                - 找到 start 及之后的第一个空闲天
                - 如果该天 <= end，则安排会议并更新并查集
             4. 路径压缩优化查找效率
        """
        events.sort(key=lambda e: e[1])  # 按结束时间排序
        mx = events[-1][1]
        fa = list(range(mx + 2))  # fa[i] = i 表示第 i 天空闲
        
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])  # 路径压缩
            return fa[x]
        
        attended = 0
        for start_day, end_day in events:
            x = find(start_day)  # 找到 start_day 及之后的第一个空闲天
            if x <= end_day:     # 如果在会议期间内
                attended += 1
                fa[x] = x + 1    # 第 x 天被占用，指向下一天
        
        return attended
