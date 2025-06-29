class SortingToolkit:
    # ░░░░░░░░░░░░░░ AcWing 785 —— 快速排序 ░░░░░░░░░░░░░░
    def quickSort(self, arr: List[int], left: int, right: int) -> None:
        """
        Hoare 分区，原地升序快速排序
            1. 选择中间元素作为基准值 pivot
            2. 使用双指针从两端向中间扫描
            3. 将小于 pivot 的元素移到左边，大于 pivot 的移到右边
            4. 递归处理左右两个子区间
        """
        if left >= right:  return
            
        pivot = arr[(left + right) >> 1]
        i, j = left, right
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                
        self.quickSort(arr, left, j)
        self.quickSort(arr, i, right)

    # ░░░░░░░░░░░░░░ AcWing 787 —— 归并排序 ░░░░░░░░░░░░░░
    def mergeSort(self, arr: List[int], left: int, right: int) -> None:
        """
        分治＋双指针合并的原地升序归并排序
            1. 将数组递归地分成两半
            2. 对左右两半分别排序
            3. 使用双指针合并两个有序数组
            4. 合并时比较两个指针所指元素，将较小的加入结果
        """
        if left == right:  return

        mid = (left + right) // 2
        self.mergeSort(arr, left, mid)
        self.mergeSort(arr, mid + 1, right)

        merged, i, j = [], left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                merged.append(arr[i])
                i += 1
            else:
                merged.append(arr[j])
                j += 1
        
        merged.extend(arr[i:mid + 1])
        merged.extend(arr[j:right + 1])
        arr[left:right + 1] = merged

    # ░░░░░░░░░░░░░░ LeetCode 215 —— 数组中的第K个最大元素 ░░░░░░░░░░░░░░
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        """ 
        使用快速选择算法查找第 k 大元素
            1. 基于快速排序的分区思想
            2. 每次分区后，基准元素会到达其最终位置
            3. 根据目标位置与基准位置的关系，只需递归一侧
            4. 第 k 大元素在升序数组中的索引是 n-k
        """
        def quickselect(left: int, right: int, idx: int) -> int:
            if left == right:  return nums[idx]
            pivot = nums[(left + right) >> 1]
            i, j = left, right
            while i <= j:
                while nums[i] < pivot:
                    i += 1
                while nums[j] > pivot:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1
            return quickselect(left, j, idx) if idx <= j else quickselect(i, right, idx)

        n = len(nums)
        return quickselect(0, n - 1, n - k)

    
    # ░░░░░░░░░░░░░░ AcWing 788 —— 逆序对的数量 ░░░░░░░░░░░░░░
    def reversePairs(self, nums: List[int], left: int, right: int) -> int:
        """
        归并分治:
            1. 递归地将区间 [left, right] 分成左右两半：[left, mid] 与 [mid+1, right]
            2. 分别统计左右两半内部的逆序对数量。
            3. 在“归并”两个有序子数组的过程中，再统计跨越左右两半的逆序对：
                   当 nums[i] > nums[j] 时（其中 i 属于左半区间，j 属于右半区间）
                   则 nums[i..mid] 全都大于 nums[j]，贡献 (mid - i + 1) 个逆序对
            4. 将左右两半归并成有序序列，保证上层递归可以正常比较
            5. 返回左右内部 + 合并阶段的逆序对之和
        """
        if left >= right:  return 0
    
        mid = (left + right) // 2
        inv_cnt = self.reversePairs(nums, left,  mid) + self.reversePairs(nums, mid + 1, right)
    
        merged, i, j = [], left, mid + 1
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                merged.append(nums[i])
                i += 1
            else:
                merged.append(nums[j])
                j += 1
                inv_cnt += (mid - i + 1)     # 左侧剩余元素均大于 nums[j]
    
        merged.extend(nums[i:mid + 1])
        merged.extend(nums[j:right + 1])
        nums[left:right + 1] = merged
        return inv_cnt
