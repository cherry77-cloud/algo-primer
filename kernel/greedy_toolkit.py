class GreedyToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 121 —— 买卖股票的最佳时机 ░░░░░░░░░░░░░░
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """
        买卖股票的最佳时机 - 只能买卖一次
             1. 从左到右枚举卖出价格 prices[i]
             2. 维护第 i 天之前的最低买入价格（prices[0] 到 prices[i-1] 的最小值）
             3. 计算当前卖出价格与最低买入价格的差值，维护最大利润
             4. pre_min 维护的是 prices[i] 左侧元素的最小值
             5. 对于每个卖出价格，买入价格应该是它之前的最低价格
        """
        pre_min = inf  # 维护当前位置之前的最低价格
        ans = 0        # 维护最大利润
        
        for price in prices:
            pre_min = min(pre_min, price)        # 更新最低买入价格
            ans = max(ans, price - pre_min)      # 更新最大利润
            
        return ans
        
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
