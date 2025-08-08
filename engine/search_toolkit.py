from collections import deque
from typing import List, Deque, Tuple, Set


class BacktrackingToolkit:
    """
    ▎1. 递归 (Recursion): 将原问题转化为规模更小但结构相同的子问题，通过解决子问题并组合其结果来解决原问题
      • 自顶向下: 从目标出发，逐层分解直至触底 | 延迟计算: 先构建调用链，后自底向上求值 | 隐式栈: 利用系统调用栈自动管理中间状态
    
    ▎2. 边界条件 (Base Case): 递归终止条件，防止无限递归的安全阀
      • 空值边界: 处理空集、空串、空树等退化情况 | 单元素边界: 不可再分的原子单位 | 数值边界: 计数器归零、索引越界等
    
    ▎3. 调用栈 (Call Stack): 保存函数调用信息的LIFO数据结构，随递归深入而增长，随递归返回而收缩
      • 压栈: 函数调用时新栈帧入栈 | 弹栈: 函数返回时栈帧出栈 | 栈溢出: 递归过深导致栈空间耗尽
    
    ▎4. 栈帧 (Stack Frame): 记录一次函数调用的完整上下文（局部变量、参数、返回地址、动态链接）
      • 每个递归层级对应一个独立栈帧 | 栈帧数量=递归深度 | 栈帧链形成从当前执行点到递归起点的完整路径

    ▎5. 回溯 (Backtracking): 系统化穷举搜索，遇到无效分支时撤销选择并尝试其他可能
      • 选择(Choose): 做出决策 | 探索(Explore): 递归探索 | 撤销(Unchoose): 恢复到选择前状态
      • 回溯是递归的特殊应用，强调状态的保存与恢复，在递归基础上增加显式状态管理
    
    ▎6. 兄弟节点 (Siblings): 同一父节点产生的多个子节点，时间上顺序执行，空间上复用相同栈位置
      • 执行时机: 父函数for循环中，兄弟A返回后栈帧弹出，才创建兄弟B的栈帧
      • 共享风险: 兄弟栈帧不同时存在，但共享父栈帧的可变对象(如path)，需撤销修改防止污染

    ▎7. 递归结构形态 (Recursion Structures): 递归执行过程形成的逻辑拓扑，由子问题分解模式和重叠程度决定
      • 递归链 (Recursion Chain): 每层仅派生 1 个子调用，执行路径呈线性链表；深度 = 调用次数，时间复杂度 O(n) ┆ 阶乘
      • 递归树 (Recursion Tree): 每层可派生 ≥2 个子调用，执行结构呈树形；节点数 ≈ 分支ᵈ，常带指数复杂度 ┆ 朴素斐波那契、全排列
      • 递归 DAG (Memoized Recursion): 备忘录共享重复子问题，将树压缩为有向无环图；节点数 ≤ 状态数，复杂度降为多项式 ┆ 记忆化斐波那契
    """
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        """
        生成所有子集: 选或不选的回溯法
           1. 对每个元素，都有选择和不选择两种情况
           2. 递归遍历所有元素，到达末尾时记录当前路径
           3. 回溯时恢复现场
        """
        n = len(nums)
        subsets = []
        path = []
        
        def dfs(u: int) -> None:
            if u == n:
                subsets.append(path[:])
                return
                
            dfs(u + 1)
            path.append(nums[u])
            dfs(u + 1)
            path.pop()
        
        dfs(0)
        return subsets
    
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    @staticmethod
    def subsets_bitmask(nums: List[int]) -> List[List[int]]:
        """
        位运算版本: 用二进制掩码表示选择状态
            1. 用 mask 的第 i 位表示是否选择 nums[i]
            2. 递归过程中构建掩码
            3. 最后根据掩码生成对应子集
        """
        n = len(nums)
        subsets = []
        
        def dfs(u: int, mask: int) -> None:
            if u == n:
                subset = []
                for i in range(n):
                    if mask & (1 << i):
                        subset.append(nums[i])
                subsets.append(subset)
                return
                
            dfs(u + 1, mask)
            dfs(u + 1, mask | (1 << u))
        
        dfs(0, 0)
        return subsets
    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列 ░░░░░░░░░░░░░░
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        """
        回溯法生成所有全排列
            1. 每个位置尝试放置所有未使用的数字
            2. 使用 visited 数组标记已使用的数字
            3. 递归填充每个位置
            4. 回溯时恢复状态
        """
        n = len(nums)
        result = []
        path = []
        visited = [False] * n
        
        def dfs(u: int) -> None:
            if u == n:
                result.append(path[:])
                return
                
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(u + 1)
                    path.pop()
                    visited[i] = False
                    
        dfs(0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列 ░░░░░░░░░░░░░░
    @staticmethod
    def permute_bitmask(nums: List[int]) -> List[List[int]]:
        """
        位运算版本: 用二进制掩码表示使用状态
            1. mask 的第 i 位为 1 表示 nums[i] 已被使用
            2. 每次选择一个未使用的数字
            3. 将该位置1表示已使用
        """
        n = len(nums)
        result = []
        path = []
        
        def dfs(u: int, mask: int) -> None:
            if u == n:
                result.append(path[:])
                return
                
            for i in range(n):
                if not (mask & (1 << i)):
                    path.append(nums[i])
                    dfs(u + 1, mask | (1 << i))
                    path.pop()
        
        dfs(0, 0)
        return result

    # ░░░░░░░░░░░░░░ LeetCode 47 · 全排列 II（有重复） ░░░░░░░░░░░░░░
    @staticmethod
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        """
        计数 + 回溯：Counter 记录剩余次数，天然去重
        """
        cnt = Counter(nums)
        n = len(nums)
        res: List[List[int]] = []
        on_path = [0] * n  # 预分配

        def dfs(i: int) -> None:
            if i == n:
                res.append(on_path.copy())
                return
            for x in cnt:
                if cnt[x] == 0:
                    continue
                cnt[x] -= 1
                on_path[i] = x
                dfs(i + 1)
                cnt[x] += 1

        dfs(0)
        return res
    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合 ░░░░░░░░░░░░░░
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        """
        生成从 1 到 n 中选取 k 个数的所有组合
            1. 使用 start 参数避免重复
            2. 从 start 开始枚举，保证递增顺序
            3. 剪枝优化: 剩余数字不够凑齐 k 个时提前返回
        """
        result: List[List[int]] = []
        path: List[int] = []
        
        def dfs(u: int, start: int) -> None:
            if u == k:
                result.append(path[:])
                return
                
            if k - u > n - start:
                return
                
            for i in range(start, n):
                path.append(i + 1)
                dfs(u + 1, i + 1)
                path.pop()

        dfs(0, 0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合 ░░░░░░░░░░░░░░
    @staticmethod
    def combine_bitmask(n: int, k: int) -> List[List[int]]:
        """
        位运算版本: 用掩码记录选中的数字
            1. cnt 记录已选择的数字个数
            2. mask 的第 i 位为 1 表示选中数字 i+1
            3. 按顺序考虑每个数字，选或不选
            4. 剪枝: 剩余数字+已选数字 < k 时返回
        """
        result: List[int] = []
        def dfs(u: int, cnt: int, mask: int) -> None:
            if cnt + n - u < k:
                return
                
            if cnt == k:
                path = []
                for i in range(n):
                    if mask & (1 << i):
                        path.append(i + 1)
                result.append(path)
                return
                
            if u == n:  
                return
                
            dfs(u + 1, cnt + 1, mask | (1 << u))
            dfs(u + 1, cnt, mask)
        
        dfs(0, 0, 0)
        return result

    # ░░░░░░░░░░░ LeetCode 22 —— 括号生成 ░░░░░░░░░░░
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        """
        生成所有有效括号组合
            1. 有效括号的规则：
               - 左括号数量不超过 n
               - 右括号数量不超过左括号数量
            2. open 记录当前左括号数量
            3. i - open 即为右括号数量
            4. 满足条件时才添加相应括号
        """
        ans: List[str] = []
        chosen: List[str] = []

        def dfs(i: int, open_count: int) -> None:
            if i == n * 2:
                ans.append(''.join(chosen))
                return
                
            if open_count < n:
                chosen.append('(')
                dfs(i + 1, open_count + 1)
                chosen.pop()
                
            if i - open_count < open_count:
                chosen.append(')')
                dfs(i + 1, open_count)
                chosen.pop()
        
        dfs(0, 0)
        return ans

    # ░░░░░░░░░░░ LeetCode 17 —— 电话号码的字母组合 ░░░░░░░░░░░
    @staticmethod
    def letterCombinations(digits: str) -> List[str]:
        """
        电话号码的字母组合
            1. 每个数字对应一组字母
            2. 依次处理每个数字
            3. 对每个数字，尝试其对应的所有字母
            4. 递归生成所有可能的组合
        """
        if not digits:
            return []
            
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ans: List[str] = []
        chosen: List[str] = []

        def dfs(i: int) -> None:
            if i == len(digits):
                ans.append(''.join(chosen))
                return
                
            idx = ord(digits[i]) - ord('0')
            for ch in MAPPING[idx]:  # 尝试该数字对应的所有字母
                chosen.append(ch)
                dfs(i + 1)
                chosen.pop()

        dfs(0)
        return ans

    # ░░░░░░░░░░░ LeetCode 79 —— 单词搜索 ░░░░░░░░░░░
    @staticmethod
    def exist(board: List[List[str]], word: str) -> bool:
        """
        在二维网格中搜索单词
            1. 优化一：检查字符频率是否满足要求
            2. 优化二：从出现次数少的一端开始搜索
            3. DFS + 回溯：标记访问过的格子
            4. 恢复现场：回溯时恢复原始值
            5. 剪枝：不匹配立即返回
        """
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):
            return False
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        m, n = len(board), len(board[0])
        
        def dfs(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:  # 匹配失败
                return False
            if k == len(word) - 1:      # 匹配成功, 处理单字符情况
                return True
            board[i][j] = ''            # 标记访问过
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):  # 相邻格子
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True  # 搜到了！
            board[i][j] = word[k]  # 恢复现场
            return False  # 没搜到
            
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))

    # ░░░░░░░░░░░ LeetCode 131 —— 分割回文串 ░░░░░░░░░░░
    @staticmethod
    def partition(s: str) -> List[List[str]]:
        """
        将字符串分割成若干回文子串
            1. 回溯框架：枚举每个分割位置
            2. 选择空间：从当前位置到字符串末尾的所有子串
            3. 剪枝条件：只有回文串才继续递归
            4. 终止条件：指针到达字符串末尾
            5. 回溯恢复：path.pop() 撤销选择
        """
        n = len(s)
        ans = []
        path = []
    
        def dfs(i: int) -> None:
            if i == n:                    # 分割完毕
                ans.append(path.copy())   # 必须复制！
                return
            
            for j in range(i, n):         # 枚举分割位置
                t = s[i:j+1]              # 候选子串
                if t == t[::-1]:          # 是回文串
                    path.append(t)        # 做出选择
                    dfs(j + 1)            # 递归剩余部分
                    path.pop()            # 撤销选择
        
        dfs(0)
        return ans

    # ░░░░░░░░░░░░░░ LeetCode 39 —— 组合总和 ░░░░░░░░░░░░░░
    @staticmethod
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
       """
       组合总和 - 完全背包问题
           1. 每个数字可以无限制重复使用
           2. 需要找出所有和为 target 的组合
           3. 剪枝优化：排序后，如果当前数字已经大于剩余值，后面的数字更大，直接返回
           4. 去重策略：先选小的再选大的，避免 [2,3] 和 [3,2] 的重复
       """
       candidates.sort()
       ans: List[List[int]] = []
       path: List[int] = []
       
       def dfs(u: int, left: int) -> None:
           if left == 0:
               ans.append(path.copy())
               return
           
           if u == len(candidates) or left < candidates[u]:
               return
           
           # 不选当前数字
           dfs(u + 1, left)
           
           # 选当前数字（注意还是传 u，允许重复使用）
           path.append(candidates[u])
           dfs(u, left - candidates[u])
           path.pop()
       
       dfs(0, target)
       return ans

    # ░░░░░░░░░░░░░░ LeetCode 51 —— N 皇后 ░░░░░░░░░░░░░░
    @staticmethod
    def solveNQueens(n: int) -> List[List[str]]:
        """
        N 皇后问题 - 经典回溯算法
            1. 逐行放置：每行必须且只能放一个皇后
            2. 剪枝条件：检查列和两条对角线是否被占用
            3. 对角线规律：
               - 主对角线(↘)：r + c 相同
               - 副对角线(↙)：r - c 相同（加偏移避免负数）
            4. 状态记录：用布尔数组记录占用情况，避免重复计算
        """
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def dfs(r: int):
            if r == n:
                ans.append([''.join(row) for row in board])
                return
            
            # 在 (r,c) 放皇后
            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]:   # 判断能否放皇后
                    board[r][c] = 'Q'
                    col[c] = diag1[r + c] = diag2[r - c] = True        # 皇后占用了 c 列和两条斜线
                    dfs(r + 1)
                    board[r][c] = '.'
                    col[c] = diag1[r + c] = diag2[r - c] = False       # 恢复现场
        
        dfs(0)
        return ans


class GridGraphToolKit:
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
    @staticmethod
    def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
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
