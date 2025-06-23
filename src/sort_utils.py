from typing import List


class SortUtils:
    # ░░░░░░░░░░░░░░ AcWing 785 —— 快速排序 ░░░░░░░░░░░░░░
    @staticmethod
    def quickSort(arr: List[int], left: int, right: int) -> None:
        """Hoare 分区，原地升序快速排序"""
        if left >= right:
            return

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

        SortUtils.quickSort(arr, left, j)
        SortUtils.quickSort(arr, i, right)

    # ░░░░░░░░░░░░░░ AcWing 787 —— 归并排序 ░░░░░░░░░░░░░░
    @staticmethod
    def mergeSort(arr: List[int], left: int, right: int) -> None:
        """分治＋双指针合并，原地升序排序"""
        if left == right:
            return

        mid = (left + right) // 2
        SortUtils.mergeSort(arr, left, mid)
        SortUtils.mergeSort(arr, mid + 1, right)

        merged, i, j = [], left, mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                merged.append(arr[i]); i += 1
            else:
                merged.append(arr[j]); j += 1
        merged.extend(arr[i:mid + 1])
        merged.extend(arr[j:right + 1])
        arr[left:right + 1] = merged

    # ░░░░░░░░░░░░░░ LeetCode 215 —— 数组中的第 K 个最大元素 ░░░░░░░░░░░░░░
    @staticmethod
    def findKthLargest(nums: List[int], k: int) -> int:
        """平均 O(n) 快速选择返回第 k 大元素"""
        def quickselect(left: int, right: int, idx: int) -> int:
            if left == right:
                return nums[idx]

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
