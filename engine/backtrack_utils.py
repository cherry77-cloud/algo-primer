from typing import List, Optional


class BacktrackingToolkit:
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
