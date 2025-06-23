from typing import List, Optional


class BacktrackingToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集 ░░░░░░░░░░░░░░
    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
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
    
    # ░░░░░░░░░░░░░░ LeetCode 78 · 子集（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def subsets_bitmask(nums: List[int]) -> List[List[int]]:
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
    
    # ░░░░░░░░░░░░░░ LeetCode 46 · 全排列（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def permute_bitmask(nums: List[int]) -> List[List[int]]:
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
        result = []
        path = []
        
        def dfs(u: int, start: int) -> None:
            if u == k:
                result.append(path[:])
                return
                
            if k - u > n - start + 1:
                return
            
            for i in range(start, n + 1):
                path.append(i)
                dfs(u + 1, i + 1)
                path.pop()
        
        dfs(0, 1)
        return result
    
    # ░░░░░░░░░░░░░░ LeetCode 77 · 组合（位运算版本）░░░░░░░░░░░░░░
    @staticmethod
    def combine_bitmask(n: int, k: int) -> List[List[int]]:
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
        """生成所有有效括号组合: 回溯枚举"""
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
