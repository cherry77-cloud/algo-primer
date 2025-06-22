from typing import List

# ============================================================
#  SortUtils · 经典数组排序 / 选择算法
# ============================================================
class SortUtils:

    # ========================================================
    #  Quick Sort  —— AcWing 789
    # ========================================================
    @staticmethod
    def quickSort(arr: List[int], left: int, right: int) -> None:
        """
        功能：对 arr[left:right] 区间进行原地升序快速排序（Hoare 分区）
        """
        if left >= right:
            return

        pivot_value = arr[(left + right) >> 1]
        i, j = left, right
        while i <= j:
            while arr[i] < pivot_value:
                i += 1
            while arr[j] > pivot_value:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        SortUtils.quickSort(arr, left, j)
        SortUtils.quickSort(arr, i, right)

    # ========================================================
    #  Merge Sort  —— AcWing 789
    # ========================================================
    @staticmethod
    def mergeSort(arr: List[int], left: int, right: int) -> None:
        """
        功能：分治＋双指针合并，对 arr[left:right] 区间做原地升序排序
        """
        if left == right:
            return

        mid = (left + right) // 2
        SortUtils.mergeSort(arr, left, mid)
        SortUtils.mergeSort(arr, mid + 1, right)

        merged = []
        i, j = left, mid + 1

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

    # ========================================================
    #  Quick Select (k-th Largest) —— LeetCode 215
    # ========================================================
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        """
        功能：快速选择，平均 O(n) 时间返回数组中的第 k 大值
        """
        def quickselect(left: int, right: int, idx: int) -> int:
            if left == right:
                return nums[idx]

            partition = nums[(left + right) >> 1]
            i, j = left, right

            while i <= j:
                while nums[i] < partition:
                    i += 1
                while nums[j] > partition:
                    j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j -= 1

            if idx <= j:
                return quickselect(left, j, idx)
            return quickselect(i, right, idx)

        n = len(nums)
        return quickselect(0, n - 1, n - k)
