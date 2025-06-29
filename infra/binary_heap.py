from heapq import heappush, heappushpop


# ░░░░░░░░░░░░░░ AcWing 839 - 索引堆 ░░░░░░░░░░░░░░
class IndexedMinHeap:
    """
    索引最小堆 - 支持通过索引删除和修改元素
    
    三个核心数组：
    - heap: 存储实际的值 
    - ph: position in heap - 第 k 个插入的元素在堆中的位置
    - hp: heap position - 堆中位置 i 的元素是第几个插入的
    """
    def __init__(self, max_size: int):
        self.max_size = max_size
        self.tot = 0  # 堆中元素总数
        self.kth = 0  # 插入的第k个元素
        self.heap = [0] * (max_size + 1)  # 堆数组
        self.ph = [0] * (max_size + 1)    # 第k个插入的元素在堆中的位置
        self.hp = [0] * (max_size + 1)    # 堆中位置i的元素是第几个插入的
            
    def heap_swap(self, a: int, b: int) -> None:
        """交换堆中两个位置的元素，同时维护索引关系"""
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
        self.hp[a], self.hp[b] = self.hp[b], self.hp[a]
        self.ph[self.hp[a]], self.ph[self.hp[b]] = a, b
    
    def _sift_up(self, p: int) -> None:
        """上浮操作"""
        while p // 2 > 0 and self.heap[p] < self.heap[p // 2]:
            self.heap_swap(p, p // 2)
            p //= 2
        
    def _sift_down(self, u: int) -> None:
        """下沉操作"""
        rt = u
        if 2 * u <= self.tot and self.heap[2 * u] < self.heap[rt]:
            rt = 2 * u
        if 2 * u + 1 <= self.tot and self.heap[2 * u + 1] < self.heap[rt]:
            rt = 2 * u + 1
        if rt != u:
            self.heap_swap(rt, u)
            self._sift_down(rt)
            
    def insert(self, x: int) -> int:
        """插入元素，返回其索引"""
        self.tot += 1
        self.kth += 1
        self.heap[self.tot] = x
        self.hp[self.tot] = self.kth
        self.ph[self.kth] = self.tot
        self._sift_up(self.tot)
        return self.kth
        
    def get_min(self) -> int:
        """获取最小值"""
        if self.tot == 0:
            raise IndexError("empty heap")
        return self.heap[1]
        
    def delete_min(self) -> int:
        """删除并返回最小值"""
        if self.tot == 0:
            raise IndexError("empty heap")
        min_val = self.heap[1]
        self.heap_swap(1, self.tot)
        self.tot -= 1
        self._sift_down(1)
        return min_val
        
    def delete(self, k: int) -> None:
        """删除第k个插入的元素"""
        pos = self.ph[k]
        self.heap_swap(pos, self.tot)
        self.tot -= 1
        self._sift_up(pos)
        self._sift_down(pos)
        
    def change(self, k: int, x: int) -> None:
        """修改第k个插入的元素的值"""
        pos = self.ph[k]
        self.heap[pos] = x
        self._sift_up(pos)
        self._sift_down(pos)


# ░░░░░░░░░░░░░░ LeetCode 295 —— 数据流的中位数 ░░░░░░░░░░░░░░
class MedianFinder:
    """
    对顶堆维护动态中位数, 使用两个堆将数据分成两半:
        - 左堆(大根堆)：存储较小的一半，堆顶是最大值
        - 右堆(小根堆)：存储较大的一半，堆顶是最小值
        
    维护两个不变量：
        1. 平衡性：len(left) - len(right) ∈ {0, 1}
        2. 有序性：max(left) ≤ min(right)
    """
    def __init__(self):
        self.left = []   # 大根堆（存负数），保存较小的一半
        self.right = []  # 小根堆，保存较大的一半
    
    def addNum(self, num: int) -> None:
        """ 添加数字的核心逻辑: 不能直接插入目标堆！必须先经过另一个堆"过滤" """
        if len(self.left) == len(self.right):
            # 两堆相等，新元素要进左堆
            # num先进右堆，弹出最小值，该值 ≤ 右堆所有元素
            heappush(self.left, -heappushpop(self.right, num))
        else:
            # 左堆多一个，新元素要进右堆
            # -num先进左堆，弹出最大值的负数，还原后 ≥ 左堆所有元素
            heappush(self.right, -heappushpop(self.left, -num))
    
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (self.right[0] - self.left[0]) / 2


class BinaryHeapToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 347 - 前K个高频元素 ░░░░░░░░░░░░░░
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        """
        统计频率 + 最小堆
            1. 使用 Counter 统计每个元素的出现频率
            2. 维护大小为 k 的最小堆
            3. 堆中保存 (频率, 元素) 元组
            4. 如果新元素频率大于堆顶，替换堆顶
            5. 最终堆中就是频率最高的 k 个元素
        """
        freq_map = Counter(nums)
        heap = []
        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:  # 当前频率大于堆顶（最小频率），替换
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        
        return [num for _, num in heap]
