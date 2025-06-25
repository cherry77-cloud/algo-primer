from typing import List, Optional
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 2 · 两数相加 ░░░░░░░░░░░░░░
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        模拟加法进位，逐位相加
            1. 创建哨兵节点 dummy，方便返回结果链表
            2. 遍历两个链表，逐位相加，同时处理进位
            3. 如果某个链表先结束，继续处理另一个链表
            4. 最后如果还有进位，需要新建节点存储
            5. 返回 dummy.next 即为结果链表头节点
        """
        cur = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next
        return dummy.next

    # ░░░░░░░░░░░░░░ LeetCode 19 · 删除链表的倒数第 N 个结点 ░░░░░░░░░░░░░░
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        快慢指针定位倒数第 N 个节点
            1. 使用哨兵节点处理删除头节点的特殊情况
            2. 快指针先走 n 步，建立 n 的间隔
            3. 快慢指针同时前进，直到快指针到达末尾
            4. 此时慢指针恰好在待删除节点的前一个位置
            5. 修改指针跳过待删除节点，完成删除
        """
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

    # ░░░░░░░░░░░░░░ LeetCode 21 · 合并两个有序链表 ░░░░░░░░░░░░░░
    # -------- 递归版本 --------
    def mergeTwoLists_recursive(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        递归合并两个有序链表
            1. 基本情况：某个链表为空，返回另一个链表
            2. 比较两个链表头节点，选择较小的作为当前节点
            3. 递归处理较小节点的 next 和另一个链表
            4. 返回较小节点，构建有序链表
            5. 递归展开后自然形成升序链表
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

    # -------- 迭代版本 --------
    def mergeTwoLists_iterative(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        迭代合并两个有序链表
            1. 创建哨兵节点，cur 指针用于构建新链表
            2. 比较两个链表当前节点，选择较小的接入新链表
            3. 移动被选中链表的指针和 cur 指针
            4. 某个链表遍历完后，将另一个链表剩余部分接入
            5. 返回哨兵节点的 next，即合并后的链表头
        """
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next

    # ░░░░░░░░░░░░░░ LeetCode 206 · 反转链表 ░░░░░░░░░░░░░░
    # -------- 递归版本 --------
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归反转链表
            1. 递归到链表末尾，最后一个节点作为新的头节点
            2. 回溯过程中，将 head.next 的 next 指向 head
            3. 断开 head 的 next 指针，避免形成环
            4. 逐层返回新的头节点
            5. 最终返回反转后的链表头节点
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    # -------- 迭代版本 --------
    def reverseList_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代反转链表
            1. pre 指向已反转部分的头，cur 指向当前处理节点
            2. 保存 cur.next 到 nxt，避免断链
            3. 将 cur.next 指向 pre，完成当前节点反转
            4. pre 和 cur 都向前移动一位
            5. 最终 pre 指向反转后的链表头
        """
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # ░░░░░░░░░░░░░░ LeetCode 876 · 链表的中间结点 ░░░░░░░░░░░░░░
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        快慢指针找中间节点
            1. slow 走一步，fast 走两步
            2. fast 到达末尾时，slow 恰好在中间
            3. 奇数长度: slow 在正中间
            4. 偶数长度: slow 在中间两个节点的第二个
            5. 返回 slow 指向的节点
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # ░░░░░░░░░░░░░░ LeetCode 234 · 回文链表 ░░░░░░░░░░░░░░
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        找中点 + 反转后半部分 + 比较
            1. 使用快慢指针找到链表中点
            2. 反转后半部分链表
            3. 同时遍历前半部分和反转后的后半部分
            4. 逐个比较节点值是否相等
            5. 全部相等则为回文，否则不是
        """
        latter = self.reverseList_iterative(self.middleNode(head))
        while latter:
            if head.val != latter.val:
                return False
            head = head.next
            latter = latter.next
        return True

    # ░░░░░░░░░░░░░░ LeetCode 160 · 相交链表 ░░░░░░░░░░░░░░
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        双指针相遇法找相交节点
            1. 两个指针分别从两个链表头开始
            2. 到达末尾后切换到另一个链表头继续
            3. 两指针走过的路径长度相同: A+B = B+A
            4. 如果相交，必在交点相遇；不相交则同时为 None
            5. 返回相遇点即为相交起始节点
        """
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

    # ░░░░░░░░░░░░░░ LeetCode 141 · 环形链表 ░░░░░░░░░░░░░░
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        快慢指针判断环
            1. slow 走一步，fast 走两步
            2. 如果有环，fast 会追上 slow
            3. 如果无环，fast 会先到达末尾
            4. 相遇即说明有环，到达末尾说明无环
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # ░░░░░░░░░░░░░░ LeetCode 142 · 环形链表 II ░░░░░░░░░░░░░░
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Floyd 判圈算法找环入口
            1. 快慢指针相遇，确认有环
            2. 数学原理：相遇点到环入口距离 = 起点到环入口距离
            3. 一个指针从头开始，一个从相遇点开始
            4. 两指针同速前进，相遇点即为环入口
            5. 无环返回 None
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:  # 相遇
                while slow is not head:  # 再走 a 步
                    slow = slow.next
                    head = head.next
                return slow
        return None

    # ░░░░░░░░░░░░░░ LeetCode 148 · 排序链表 ░░░░░░░░░░░░░░
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        归并排序链表
            1. 递归基: 空链表或单节点直接返回
            2. 快慢指针找中点，断开成两个子链表
            3. 递归排序左右两个子链表
            4. 合并两个有序链表得到结果
        """
        if not head or not head.next:  return head

        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeTwoLists_iterative(left, right)

    # ░░░░░░░░░░░░░░ LeetCode 24 · 两两交换链表中的节点 ░░░░░░░░░░░░░░
    # -------- 迭代版本 --------
    def swapPairs_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        迭代交换相邻节点
            1. 使用哨兵节点简化边界处理
            2. 维护 4 个指针: node0(前驱)、node1、node2(待交换)、node3(后继)
            3. 交换 node1 和 node2：node0->node2->node1->node3
            4. 更新指针，处理下一对节点
            5. 返回哨兵节点的 next
        """
        node0 = dummy = ListNode(next=head)
        node1 = head
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node0.next = node2
            node2.next = node1
            node1.next = node3

            node0 = node1
            node1 = node3
        return dummy.next

    # -------- 递归版本 --------
    def swapPairs_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        递归交换相邻节点
            1. 递归基: 空链表或单节点直接返回
            2. 保存前两个节点和第三个节点的引用
            3. 递归处理第三个节点开始的子链表
            4. 交换前两个节点，node2 指向 node1
            5. node1 指向递归处理后的子链表，返回 node2
        """
        if head is None or head.next is None:
            return head

        node1 = head
        node2 = head.next
        node3 = node2.next

        node1.next = self.swapPairs_recursive(node3)
        node2.next = node1
        return node2

    # ░░░░░░░░░░░░░░ LeetCode 23 · 合并 K 个升序链表 ░░░░░░░░░░░░░░
    # -------- 堆方法 --------
    def mergeKLists_heap(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """
        最小堆合并 K 个链表
            1. 定义节点比较方法，按 val 值比较
            2. 将所有链表头节点加入最小堆
            3. 每次取出最小节点接入结果链表
            4. 如果该节点有后继，将后继加入堆
            5. 重复直到堆为空，时间 O(nlogk)
        """
        ListNode.__lt__ = lambda a, b: a.val < b.val
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node
            cur = cur.next
        return dummy.next

    # -------- 分治方法 --------
    def mergeKLists_divideConquer(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        """
        分治法合并 K 个链表
            1. 递归基: 0 个返回 None，1 个直接返回
            2. 将链表数组分成两半
            3. 递归合并左半部分和右半部分
            4. 将两个合并结果再合并
            5. 时间 O(nlogk)，每层合并 O(n)，共 logk 层
        """
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]
        left = self.mergeKLists_divideConquer(lists[: m // 2])
        right = self.mergeKLists_divideConquer(lists[m // 2 :])
        return self.mergeTwoLists_iterative(left, right)
