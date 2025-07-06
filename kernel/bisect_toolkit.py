class BinarySearchTemplate:
    """
    1. rightmost_red — 适用于 True ... True | False ... False 模式
       - 序列前半部分都是 True（红区），后半部分都是 False（蓝区）
       - 返回最后一个 True 的位置
    
    2. leftmost_blue — 适用于 False ... False | True ... True 模式
       - 序列前半部分都是 False（红区），后半部分都是 True（蓝区）
       - 返回第一个 True 的位置
    核心思想：任何满足"单调性"的布尔函数都可以使用
    """
    @staticmethod
    def rightmost_red(left: int, right: int, is_red: Callable[[int], bool]) -> int:
        """
        示例序列:  [T, T, T, T, F, F, F]
                            ↑
                        返回这个位置
        使用右中位数: (left + right + 1) // 2, 避免死循环
        case 1: mid 位置仍在红区, 更新 left = mid，保留 mid 作为候选答案
        case 2: mid 位置已经在蓝区, 更新 right = mid - 1，排除 mid
        """
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):
                left = mid
            else:
                right = mid - 1
        return left
    
    @staticmethod
    def leftmost_blue(left: int, right: int, is_blue: Callable[[int], bool]) -> int:
        """
        示例序列:  [F, F, F, T, T, T, T]
                            ↑
                        返回这个位置
        # case 1: mid 位置已经在蓝区, 说明答案在 mid 或 mid 左边, 更新 right = mid，保留 mid 作为候选答案
        # case 2: mid 位置仍在红区, 说明答案一定在 mid 右边, 更新 left = mid + 1，排除 mid
        """
        while left < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid + 1
        return left

    @staticmethod
    def float_binary_search(
        left: float, 
        right: float, 
        check: Callable[[float], bool], 
        eps: float = 1e-9) -> float:
    """
    浮点数二分查找模板 - 寻找满足条件的最小值
    在连续区间 [left, right] 中找到满足 check(x) = True 的最小 x
    """
    while right - left > eps:
        mid = (left + right) / 2
        if check(mid):
            right = mid  # mid 满足条件，答案在 [left, mid]
        else:
            left = mid   # mid 不满足条件，答案在 [mid, right]
    return left  # 或 return right，差值小于 eps


class BinarySearchUtils:
    # ░░░░░░░░░░░░░░ LeetCode 34 —— 在排序数组中查找元素的第一个和最后一个位置 ░░░░░░░░░░░░░░
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        """ 使用两次二分：找最后一个红区元素 和 第一个蓝区元素 """
        def find_last_red(left: int = 0, right: int = len(nums) - 1) -> int:
            """ 找最后一个 <= target 的位置 """
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
        
        def find_first_blue(left: int = 0, right: int = len(nums) - 1) -> int:
            """ 找第一个 >= target 的位置 """
            while left < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        l1, l2 = find_last_red(0, len(nums) - 1), find_first_blue(0, len(nums) - 1)
        if not nums or nums[l1] != target:
            return [-1, -1]
        return [l2, l1]

    # ░░░░░░░░░░░ LeetCode 153 —— 寻找旋转排序数组中的最小值 ░░░░░░░░░░░
    @staticmethod
    def findMin(nums: List[int]) -> int:
        """
        旋转排序数组中的最小值
             1. 旋转数组特点：存在一个断点，左边部分 > 右边部分
             2. 二分查找：比较 mid 和末尾元素
             3. 如果 nums[mid] <= nums[-1]，说明 mid 在右半部分，最小值在 mid 或左边
             4. 如果 nums[mid] > nums[-1]，说明 mid 在左半部分，最小值在右边
             5. 收缩区间直到找到最小值
        时间复杂度：O(log n)，空间复杂度：O(1)
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid      # mid 可能是最小值，保留
            else:
                left = mid + 1   # mid 在左半部分，最小值在右边
        return nums[left]

    # ░░░░░░░░░░░ LeetCode 33 —— 搜索旋转排序数组 ░░░░░░░░░░░
    @staticmethod
    def search_rotated(nums: List[int], target: int) -> int:
        """
        红 / 蓝 区划分由下式给出
            is_red(i) = (x <= target) ^ (x > pivot) ^ (target > pivot), 其中 pivot = nums[-1]
        · 若 target 在右段：
            红区 = 左段全部 + 右段中 x <= target
            蓝区 = 右段中 x > target
        · 若 target 在左段：
            红区 = 左段中 x <= target
            蓝区 = 其余元素
        """
        left, right = 0, len(nums) - 1
        pivot = nums[-1]
        def is_red(i: int) -> bool:
            x = nums[i]
            return (x <= target) ^ (x > pivot) ^ (target > pivot)
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1: 红区→向右扩
                left = mid
            else:                        # case 2: 蓝区→向左收
                right = mid - 1
        return left if nums[left] == target else -1

    # ░░░░░░░░░░░ LeetCode 74 —— 搜索二维矩阵 ░░░░░░░░░░░
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        """
        搜索二维矩阵（每行递增，下一行首元素大于上一行末元素）
             1. 将二维矩阵视为一维有序数组
             2. 坐标转换：一维下标 i → 二维坐标 (i//n, i%n)
             3. 使用标准二分查找，找到最后一个 <= target 的位置
             4. 检查该位置的值是否等于 target
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid // n][mid % n] <= target:
                left = mid
            else:
                right = mid - 1
        return matrix[left // n][left % n] == target

    # ░░░░░░░░░░░ LeetCode 240 —— 搜索二维矩阵 II ░░░░░░░░░░░
    @staticmethod
    def searchMatrixII(matrix: List[List[int]], target: int) -> bool:
        """
        搜索二维矩阵 II（每行递增，每列递增）, 核心思想是Z字形搜索
             1. 从左下角或右上角开始（这里选择左下角）
             2. 当前元素比 target 小：只能向右移动（j++）
             3. 当前元素比 target 大：只能向上移动（i--）
             4. 每次比较可以排除一行或一列，类似 BST 的查找
        """
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0  # 从左下角开始
        
        while i >= 0 and j < n:
            x = matrix[i][j]
            if x < target:
                j += 1   # 当前值太小，向右移动
            elif x > target:
                i -= 1   # 当前值太大，向上移动
            else:
                return True
                
        return False


class BinaryAnswerUtils:
    # ░░░░░░░░░░░ LeetCode 274 —— H 指数 ░░░░░░░░░░░
    @staticmethod
    def hIndex(citations: List[int]) -> int:
        """
        二分答案：最大 h 使得“引用次数 ≥ h”的论文数 ≥ h
        红区: cnt ≥ h  —— 当前 h 可行，尝试更大  
        蓝区: cnt < h  —— 当前 h 不可行，调小
        """
        left, right = 0, max(citations)
        def is_red(h: int) -> bool:
            cnt = sum(cite >= h for cite in citations)
            return cnt >= h              # case 1：红区
        while left < right:
            mid = (left + right + 1) // 2
            if is_red(mid):              # case 1：红区→向右扩
                left = mid
            else:                        # case 2：蓝区→向左收
                right = mid - 1
        return left
