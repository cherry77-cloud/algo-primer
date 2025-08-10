class MemoizationSearch:
    """
    记忆化搜索是一种 **空间换时间** 的动态规划优化技术，本质上通过缓存「函数参数 → 结果」键值对，消除递归中的子问题重叠
    • 状态空间: 函数全部实参组合构成的集合  
    • 解空间: 每个状态对应的唯一计算结果  
    • 缓存结构 -> 哈希表 memo : (params_tuple) → result
      └► 键 Key = 递归函数的入参元组  
      └► 值 Value = 该入参对应的返回值
    - 递归调用树: 原始递归形成的大量重复子树  
    - 状态转移图: 去重后得到的有向无环图 
        • 顶点: 所有可达状态  
        • 边: 状态间依赖 (u,v) 表示求 u 先求 v  
        • 由于递归无后效性，图必然无环，可视为动态规划拓扑序
        
    map<pair<int, int>, int> memo;
    auto dfs = [&](this auto&& self, int i, int c) -> int {
        if (i < 0 || c <= 0) return 0;
        auto key = make_pair(i, c);
        if (memo.contains(key)) return memo[key];
        int not_take = self(i - 1, c);
        int take = 0;
        if (c >= w[i]) {
            take = v[i] + self(i - 1, c - w[i]);
        }
        return memo[key] = max(take, not_take);
    };
    """
    # ░░░░░░░░░░░░░░ 0-1 背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], cap: int) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0 or c <= 0:
                return 0
            not_take = dfs(i - 1, c)
            if c >= weights[i]:
                take = values[i] + dfs(i - 1, c - weights[i])
                return max(take, not_take)
            return not_take
        return dfs(n - 1, cap)

    # ░░░░░░░░░░░░░░ 完全 / 无界背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_unbounded(weights: List[int], values: List[int], cap: int) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0 or c <= 0:
                return 0
            not_take = dfs(i - 1, c)
            if c >= weights[i]:
                # 取当前物品后 i 不变，可再次选择
                take = values[i] + dfs(i, c - weights[i])
                return max(take, not_take)
            return not_take
        return dfs(n - 1, cap)

    # ░░░░░░░░░░░░░░ 二维约束背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_2d(
        weights: List[int],
        volumes: List[int],
        values: List[int],
        max_w: int,
        max_v: int,
    ) -> int:
        n = len(weights)
        @cache
        def dfs(i: int, w_rem: int, v_rem: int) -> int:
            if i < 0 or w_rem <= 0 or v_rem <= 0:
                return 0
            not_take = dfs(i - 1, w_rem, v_rem)
            if w_rem >= weights[i] and v_rem >= volumes[i]:
                take = values[i] + dfs(
                    i - 1,
                    w_rem - weights[i],
                    v_rem - volumes[i],
                )
                return max(take, not_take)
            return not_take
        return dfs(n - 1, max_w, max_v)

    # ░░░░░░░░░░░░░░ LeetCode 120 —— 三角形最小路径和 ░░░░░░░░░░░░░░
    @staticmethod
    def minimumTotal(triangle: List[List[int]]) -> int:
        """
        三角形自顶向下最小路径和（记忆化搜索）
             1. dfs(i, j) 表示从位置 (i,j) 到底部的最小路径和
             2. 到达底部时，返回当前位置的值
             3. 否则，可以走到 (i+1,j) 或 (i+1,j+1)
             4. 选择两条路径中的最小值，加上当前值
             5. 使用 @cache 装饰器自动记忆化
        """
        n = len(triangle)
        @cache
        def dfs(i: int, j: int) -> int:
            if i == n - 1:
                return triangle[i][j]
            return min(dfs(i + 1, j), dfs(i + 1, j + 1)) + triangle[i][j]
        return dfs(0, 0)

    # ░░░░░░░░░░░░░░ LeetCode 63 —— 不同路径 II ░░░░░░░░░░░░░░
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
        """
        带障碍物的矩阵路径计数（记忆化搜索）
             1. dfs(i, j) 表示从 (0,0) 到 (i,j) 的路径数量
             2. 边界处理：越界或遇到障碍物返回 0
             3. 起点处理：如果是起点且无障碍返回 1
             4. 每个位置可以从上方或左方到达（如果无障碍）
             5. 路径数等于两个方向路径数之和
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or obstacleGrid[i][j]:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░░░░ LeetCode 329 —— 矩阵中的最长递增路径 ░░░░░░░░░░░░░░
    @staticmethod
    def longestIncreasingPath(matrix: List[List[int]]) -> int:
        """
        矩阵最长递增路径（四方向 DFS + 记忆化）
             1. dfs(i, j) 表示从 (i,j) 开始的最长递增路径长度
             2. 尝试向四个方向扩展：上下左右
             3. 只能走到值更小的格子（严格递减）
             4. 取所有可行方向的最大值，加上当前格子（长度+1）
             5. 枚举所有起点，返回全局最大值
        """
        DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        @cache
        def dfs(i: int, j: int) -> int:
            best = 1
            for dx, dy in DIRS:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))
            return best
        return max(dfs(i, j) for i in range(m) for j in range(n))


class KnapsackToolkit:
    # ░░░░░░░░░░░░░░ AcWing 2 —— 0-1 背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_01(volumes: List[int], values: List[int], capacity: int) -> int:
        """
        一维滚动数组优化的 0-1 背包
             1. 初始化 dp[j] 表示容量为 j 时的最大价值
             2. 遍历每个物品, 从大到小枚举容量（避免重复选择）
             3. 对每个容量 j, 比较不选当前物品和选当前物品的价值
             4. dp[j] = max(dp[j], dp[j-vol] + val) 状态转移
             5. 返回 dp[capacity] 即为最大价值
        """
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ AcWing 3 —— 完全背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_complete(volumes: List[int], values: List[int], capacity: int) -> int:
        """
        一维正序遍历的完全背包
             1. 初始化 dp[j] 表示容量为 j 时的最大价值
             2. 遍历每个物品，从小到大枚举容量（允许重复选择）
             3. 对每个容量 j，考虑再选一个当前物品的收益
             4. dp[j] = max(dp[j], dp[j-vol] + val) 状态转移
             5. 返回 dp[capacity] 即为最大价值
        """
        dp = [0] * (capacity + 1)
        for vol, val in zip(volumes, values):
            for j in range(vol, capacity + 1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ AcWing 8 —— 二维 0-1 背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_2d(
        volumes: List[int],
        weights: List[int],
        values: List[int],
        max_volume: int,
        max_weight: int
    ) -> int:
        """
        体积重量双限制的二维 0-1 背包
             1. 初始化 dp[v][w] 表示体积 v、重量 w 限制下的最大价值
             2. 遍历每个物品，倒序枚举体积和重量（避免重复选择）
             3. 对每个状态 (v,w)，比较不选和选当前物品的价值
             4. dp[v][w] = max(dp[v][w], dp[v-vol][w-wgt] + val)
             5. 返回 dp[max_volume][max_weight] 即为最大价值
        """
        dp = [[0] * (max_weight + 1) for _ in range(max_volume + 1)]
        for vol, wgt, val in zip(volumes, weights, values):
            for v in range(max_volume, vol - 1, -1):
                for w in range(max_weight, wgt - 1, -1):
                    dp[v][w] = max(dp[v][w], dp[v - vol][w - wgt] + val)
        return dp[max_volume][max_weight]

    # ░░░░░░░░░░░░░░ AcWing 4 —— 多重背包 ░░░░░░░░░░░░░░
    @staticmethod
    def knapsack_multiple(
        volumes: List[int],
        values: List[int],
        counts: List[int],
        capacity: int
    ) -> int:
        """
        二进制拆分优化的多重背包
             1. 将每种物品按二进制拆分成若干个新物品
             2. 拆分策略: 1, 2, 4, ..., 2^k, 剩余部分
             3. 这样任意数量都可以由拆分后的物品组合得到
             4. 将拆分后的物品作为 0-1 背包问题求解
        """
        items: List[Tuple[int, int]] = []
        for v, w, s in zip(volumes, values, counts):
            k = 1
            while k <= s:
                items.append((v * k, w * k))
                s -= k
                k <<= 1
            if s:
                items.append((v * s, w * s))
        dp = [0] * (capacity + 1)
        for vol, val in items:
            for j in range(capacity, vol - 1, -1):
                dp[j] = max(dp[j], dp[j - vol] + val)
        return dp[capacity]

    # ░░░░░░░░░░░░░░ LeetCode 322 —— 零钱兑换 ░░░░░░░░░░░░░░
    @staticmethod
    def coinChange(coins: List[int], amount: int) -> int:
        """
        完全背包思想的硬币找零（记忆化搜索）
             1. dfs(i, c) 表示使用前 i 种硬币凑出金额 c 的最少硬币数
             2. 对每种硬币，可以选择不用或继续使用
             3. 不用：dfs(i-1, c)，转向下一种硬币
             4. 继续用：dfs(i, c-coins[i]) + 1，硬币数加一
             5. 使用记忆化避免重复计算，返回最小值
        """
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 0 if c == 0 else inf
            not_take = dfs(i - 1, c)
            take = inf
            if c >= coins[i]:
                take = dfs(i, c - coins[i]) + 1
            return min(not_take, take)
        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

    # ░░░░░░░░░░░░░░ LeetCode 279 —— 完全平方数 ░░░░░░░░░░░░░░
    @staticmethod
    def numSquares(n: int) -> int:
        """
        完全背包求最少完全平方数
             1. f[j] 表示组成 j 的最少完全平方数个数
             2. 枚举所有可能的平方数 i^2 (i from 1 to √n)
             3. 对每个数 j，尝试减去一个平方数 i^2
             4. f[j] = min(f[j], f[j-i^2] + 1) 状态转移
             5. 返回 f[n] 即为答案
        """
        f = [0] + [inf] * n
        for i in range(1, isqrt(n) + 1):
            for j in range(i * i, n + 1):
                f[j] = min(f[j], f[j - i * i] + 1)
        return f[n]


class SubsequenceDPToolkit:
    # ░░░░░░░░░░░ LeetCode 300 —— 最长递增子序列 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLIS(nums: List[int]) -> int:
        """
        贪心 + 二分查找求 LIS 长度
             1. tails[i] 表示长度为 i+1 的递增子序列的最小末尾值
             2. 遍历每个数字，二分查找其在 tails 中的位置
             3. 如果大于所有元素，追加到末尾（子序列变长）
             4. 否则更新对应位置（保持该长度的最小末尾）
             5. tails 长度即为 LIS 长度
        """
        tails: List[int] = []
        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x
        return len(tails)

    # ░░░░░░░░░░░ LeetCode 1143 —— 最长公共子序列 ░░░░░░░░░░░
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        """
        最长公共子序列 LCS（记忆化搜索）
             1. dfs(i, j) 表示 text1[0:i+1] 和 text2[0:j+1] 的 LCS 长度
             2. 边界: 任一索引小于 0 时返回 0
             3. 如果当前字符相等，LCS 长度 = dfs(i-1, j-1) + 1
             4. 如果不等，取两种情况最大值：跳过 text1[i] 或跳过 text2[j]
             5. 使用记忆化避免重复计算
        """
        m, n = len(text1), len(text2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░ LeetCode 72 —— 编辑距离 ░░░░░░░░░░░
    @staticmethod
    def minDistance(word1: str, word2: str) -> int:
        """
        编辑距离（三种操作的记忆化搜索）
             1. dfs(i, j) 表示 word1[0:i+1] 转换为 word2[0:j+1] 的最少操作数
             2. 边界: i < 0 返回 j + 1（插入），j < 0 返回 i+1（删除）
             3. 字符相等时无需操作: dfs(i-1, j-1)
             4. 字符不等时取三种操作最小值：
                - 删除 word1[i]: dfs(i-1, j) + 1
                - 插入字符: dfs(i, j-1) + 1
                - 替换 word1[i]: dfs(i-1, j-1) + 1
        """
        m, n = len(word1), len(word2)
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                return dfs(i - 1, j - 1)
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░ LeetCode 10 —— 正则表达式匹配 ░░░░░░░░░░░
    @staticmethod
    def isMatch(s: str, p: str) -> bool:
        """
        正则表达式匹配（支持 . 和 * 的记忆化搜索）
             1. dfs(i, j) 判断 s[0:i+1] 与 p[0:j+1] 是否匹配
             2. 边界: 模式串耗尽时，字符串也必须耗尽
             3. 字符串耗尽时，模式串只能是 x*y*z* 形式
             4. 遇到 '*' 时有两种选择：
                - 跳过 "x*" 两个字符（匹配 0 次）
                - 若前一字符匹配，消费 s[i]，继续停在 '*'（匹配多次）
             5. 普通字符或 '.' 必须精确匹配才能继续
        """
        m, n = len(s), len(p)
        @cache
        def dfs(i: int, j: int) -> bool:
            if j < 0:                      # 模式串已耗尽
                return i < 0
            if i < 0:                      # s 耗尽，只能匹配形如 a*b*c*...
                return p[j] == '*' and dfs(i, j - 2)
            if p[j] == '*':
                # 1) 跳过 "x*" 两字符
                if dfs(i, j - 2):
                    return True
                # 2) 若当前字符可匹配，则消费 s[i]，仍停在 '*' 处继续匹配
                if p[j - 1] in {s[i], '.'}:
                    return dfs(i - 1, j)
                return False
            else:
                if p[j] in {s[i], '.'}:
                    return dfs(i - 1, j - 1)
                return False
        return dfs(m - 1, n - 1)

    # ░░░░░░░░░░░ LeetCode 139 —— 单词拆分（DP） ░░░░░░░░░░░
    @staticmethod
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        """
        动态规划：
            1. f[i] 表示 s[:i] 是否可由字典组成
            2. 只需回看长度 ≤ max_len 的前缀
            3. 若存在 j < i 使得 f[j] = True 且 s[j:i] 在字典中，则 f[i] = True
        """
        max_len = max(map(len, wordDict))
        words = set(wordDict)

        n = len(s)
        f = [True] + [False] * n
        for i in range(len(s) + 1):
            start = max(0, i - max_len)
            for j in range(start, i):
                if s[j: i] in words and f[j]:
                    f[i] = True
                    break
        return f[n]


class SubarrayDPToolkit:
    # ░░░░░░░░░░░ LeetCode 53 —— 最大子数组和 ░░░░░░░░░░░
    @staticmethod
    def maxSubArray(nums: List[int]) -> int:
        """
        Kadane 算法求最大子数组和
             1. f[i] 表示以 nums[i] 结尾的最大子数组和
             2. 对每个位置，可以接续前面的子数组或重新开始
             3. f[i] = max(f[i-1], 0) + nums[i]
             4. 如果前面的和为负，不如重新开始
             5. 答案是所有 f[i] 的最大值
        """
        f = [0] * len(nums)
        f[0] = nums[0]
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)

    # ░░░░░░░░░░░ LeetCode 152 —— 乘积最大子数组 ░░░░░░░░░░░
    @staticmethod
    def maxProduct(nums: List[int]) -> int:
        """
        最大子数组乘积（考虑负数的影响）
             1. f_max[i] 表示以 nums[i] 结尾的最大乘积
             2. f_min[i] 表示以 nums[i] 结尾的最小乘积
             3. 由于负数乘负数会变正，需要同时维护最大值和最小值
             4. f_max[i] = max(f_max[i-1] * nums[i], f_min[i-1] * nums[i], nums[i])
             5. f_min[i] = min(f_max[i-1] * nums[i], f_min[i-1] * nums[i], nums[i])
        """
        n = len(nums)
        f_max = [0] * n
        f_min = [0] * n
        f_max[0] = f_min[0] = nums[0]
        
        for i in range(1, n):
            x = nums[i]
            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x)
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x)
            
        return max(f_max)


class StateMachineToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 121 —— 买卖股票的最佳时机 ░░░░░░░░░░░░░░
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """
        买卖股票的最佳时机 - 只能买卖一次
             1. 从左到右枚举卖出价格 prices[i]
             2. 维护第 i 天之前的最低买入价格（prices[0] 到 prices[i-1] 的最小值）
             3. 计算当前卖出价格与最低买入价格的差值，维护最大利润
             4. pre_min 维护的是 prices[i] 左侧元素的最小值
        """
        pre_min = inf  # 维护当前位置之前的最低价格
        ans = 0        # 维护最大利润
        
        for price in prices:
            pre_min = min(pre_min, price)        # 更新最低买入价格
            ans = max(ans, price - pre_min)      # 更新最大利润
            
        return ans
