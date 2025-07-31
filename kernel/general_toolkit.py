class GeneralToolkit:
    # ░░░░░░░░░░░ LeetCode 169 —— 多数元素 ░░░░░░░░░░░
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        """
        Boyer-Moore 算法: 找出数组中出现次数超过 n/2 的元素
        核心思想: 不同元素相互抵消，最后剩下的就是多数元素
            1. 遇到相同元素：计数 +1（支持者）
            2. 遇到不同元素：计数 -1（反对者）
            3. 计数归零时：更换候选人
            4. 最终候选人必定是多数元素
        """
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += (1 if num == candidate else -1)
            
        return candidate

    # ░░░░░░░░░░░ LeetCode 41 —— 缺失的第一个正数 ░░░░░░░░░░░
    @staticmethod
    def firstMissingPositive(nums: List[int]) -> int:
        """
        原地哈希法: 将数字放到"应该在"的位置上实现 O(1) 空间查找
            1. 核心思想 → 把值 x 放到索引 x-1 的位置
            2. 座位类比:
               • 学生 = 数字值
               • 座位 = 数组索引
               • 目标 = 学号为 i 的学生坐在第 i-1 个座位
            3. 交换条件: 1 ≤ nums[i] ≤ n 且 nums[i] ≠ nums[nums[i]-1]
            4. 两轮扫描:
               • 第一轮: 持续交换直到每个位置稳定
               • 第二轮: 找第一个"学号≠座位号+1"的位置
        """
        n = len(nums)
        for i in range(n):
            # 如果当前学生的学号在 [1,n] 中，但（真身）没有坐在正确的座位上
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # 那么就交换 nums[i] 和 nums[j]，其中 j 是 i 的学号
                j = nums[i] - 1  # 减一是因为数组下标从 0 开始
                nums[i], nums[j] = nums[j], nums[i]
        
        # 找第一个学号与座位编号不匹配的学生
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 所有学生都坐在正确的座位上
        return n + 1
        
    # ░░░░░░░░░░░ LeetCode 54 —— 螺旋矩阵 ░░░░░░░░░░░
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        """
        螺旋遍历矩阵: 按照螺旋顺序返回矩阵中的所有元素
        核心思想: 使用方向数组控制遍历方向，遇到边界或已访问元素时转向
            1. 定义四个方向：右→下→左→上
            2. 遍历每个位置，标记为已访问（设为None）
            3. 尝试按当前方向前进，如果越界或遇到已访问元素则转向
            4. 继续遍历直到访问完所有元素
        """
        DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)  # 右，下，左，上
        m, n = len(matrix), len(matrix[0])
        ans: List[int] = []
        i = j = di = 0  # 当前位置(i,j)和方向索引di
        
        for _ in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = None  # 标记为已访问
            x, y = i + DIRS[di][0], j + DIRS[di][1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4  # 转向下一个方向
            
            # 更新位置
            i += DIRS[di][0]
            j += DIRS[di][1]
            
        return ans
