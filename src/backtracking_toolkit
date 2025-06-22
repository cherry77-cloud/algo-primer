from typing import List, Optional
from functools import cache


class BacktrackingToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        path = []
        
        def dfs(u: int) -> None:
            if u == n:
                result.append(path[:])
                return

            dfs(u + 1)
            path.append(nums[u])
            dfs(u + 1)
            path.pop()  # 回溯
        
        dfs(0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def subsets_bitmask(nums: List[int]) -> List[List[int]]:
        """
        功能：返回数组的所有子集（幂集）
        方法：位运算法
        """
        n = len(nums)
        result = []
        
        def dfs(u: int, mask: int) -> None:
            if u == n:
                subset = []
                for i in range(n):
                    if mask & (1 << i):
                        subset.append(nums[i])
                result.append(subset)
                return
            
            dfs(u + 1, mask)              # 不选第u个元素
            dfs(u + 1, mask | (1 << u))   # 选择第u个元素
        
        dfs(0, 0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列 ░░░░░░░░░░░░░░
    @staticmethod
    def permute(nums: List[int]) -> List[List[int]]:
        """
        功能：返回数组的所有排列
        方法：回溯法
        """
        n = len(nums)
        result = []
        path = []
        visited = [False] * n
        
        def dfs(u: int) -> None:
            # u: 当前要填充的位置（深度）
            if u == n:
                result.append(path[:])  # 找到一个完整排列
                return
            
            # 枚举当前位置 u 可以放什么元素
            for i in range(n):
                if not visited[i]:           # 元素 nums[i] 还没被使用
                    visited[i] = True        # 标记使用
                    path.append(nums[i])     # 放入路径
                    dfs(u + 1)               # 递归到下一位置
                    path.pop()               # 回溯：移除选择
                    visited[i] = False       # 回溯：取消标记
        
        dfs(0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def permute_bitmask(nums: List[int]) -> List[List[int]]:
        """
        功能：返回数组的所有排列
        方法：位运算法
        """
        n = len(nums)
        result = []
        path = []
        
        def dfs(u: int, mask: int) -> None:
            # u: 当前位置, mask: 已使用元素的位掩码
            if u == n:
                result.append(path[:])
                return
            
            # 枚举当前位置可以放什么元素
            for i in range(n):
                if not (mask & (1 << i)):           # 第 i 个元素未使用
                    path.append(nums[i])
                    dfs(u + 1, mask | (1 << i))     # 标记第 i 个元素已使用
                    path.pop()
        
        dfs(0, 0)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合 ░░░░░░░░░░░░░░
    @staticmethod
    def combine(n: int, k: int) -> List[List[int]]:
        """
        功能：返回 [1, n] 中所有可能的 k 个数的组合
        方法：回溯法
        """
        result = []
        path = []
        
        def dfs(u: int, start: int) -> None:
            # u: 当前已选择的元素个数
            # start: 下一个可以选择的元素起始位置（保证有序，避免重复）
            
            if u == k:                      # 已选够 k 个元素
                result.append(path[:])      # 记录当前组合
                return
            
            # 剪枝：剩余元素不足以凑够 k 个
            if k - u > n - start + 1:
                return
            
            # 枚举下一个要选择的元素
            for i in range(start, n + 1):     # 从 start 开始，保证选择顺序
                path.append(i)                # 选择元素 i
                dfs(u + 1, i + 1)             # 递归：已选 u+1 个，下次从 i+1 开始
                path.pop()                    # 回溯：撤销选择
        
        dfs(0, 1)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def combine_bitmask(n: int, k: int) -> List[List[int]]:
        """
        功能：返回 [1, n] 中所有可能的 k 个数的组合
        方法：位运算法
        """
        result = []
        
        def dfs(u: int, cnt: int, mask: int) -> None:
            # u: 当前考虑的元素编号（第u个元素）
            # cnt: 当前已选择的元素个数
            # mask: 位掩码，记录哪些元素被选中
            
            # 剪枝：剩余元素不足以凑够 k 个
            if cnt + n - u < k:
                return  # 已选cnt个 + 剩余(n-u)个 < k个，无解
            
            if cnt == k:                       # 已选够 k 个元素
                path = []
                for i in range(n):
                    if mask & (1 << i):        # 检查第i位是否为1
                        path.append(i + 1)     # 元素 i+1 被选中
                result.append(path)
                return
            
            if u == n:
                return  # 所有元素都考虑完了
            
            # 对第 u 个元素的两种选择：
            dfs(u + 1, cnt + 1, mask | (1 << u))   # 选择第u个元素
            dfs(u + 1, cnt, mask)                  # 不选第u个元素
        
        dfs(0, 0, 0)
        return result
