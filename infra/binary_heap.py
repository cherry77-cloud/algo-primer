class BinaryHeapToolkit:
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
