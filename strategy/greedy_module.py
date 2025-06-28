from typing import List, Tuple, Optional


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
        时间复杂度：O(nlogn)，空间复杂度：O(1)
        """
        intervals.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
        ans = []
        
        for p in intervals:
            if ans and p[0] <= ans[-1][1]:  # 可以合并
                ans[-1][1] = max(ans[-1][1], p[1])  # 更新右端点最大值
            else:  # 不相交，无法合并
                ans.append(p)  # 新的合并区间
        return ans
