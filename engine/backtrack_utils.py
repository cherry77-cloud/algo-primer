from typing import List, Optional


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

    function backtrack(path, choices):
        # A. stack frame created; `path` is inherited from the parent call
        if goalReached(path):
            results.append(copy(path))       # copy is essential!
            return
    
        # B. iterate over every available option (horizontal expansion)
        for each choice in choices:
            # C. about to mutate shared state
            path.append(choice)              # Action 1: make a choice
    
            # D. state updated; descend to next level
            backtrack(path, nextChoices(choice, path))  # Action 2: recurse
    
            # E. child call has returned; restore state
            path.pop()                       # Action 3: undo the choice
    
        # F. all options explored for this frame; return to the caller
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
        result = []
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
            if u == n:  return
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
        if not digits:  return []
            
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
