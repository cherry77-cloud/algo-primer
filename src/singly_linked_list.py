from typing import List, Optional
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListToolkit:

    # --------------------------------------------------------
    #  LeetCode 2 · 两数相加
    # --------------------------------------------------------
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 将两个链表表示的数字相加, 每个节点存储一位数字（逆序存储）
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

    # --------------------------------------------------------
    #  LeetCode 19 · 删除链表的倒数第 N 个结点
    # --------------------------------------------------------
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        功能: 删除链表倒数第 n 个节点, 并返回链表头节点
        技巧: 快慢指针
        """
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

    # ========================================================
    #  LeetCode 21 · 合并两个有序链表
    # ========================================================
    # -------- 递归版本 --------
    def mergeTwoLists_recursive(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 将两个升序链表合并为一个新的升序链表
        方法: 递归比较两个链表的头节点, 选择较小节点
        """
        if list1 is None:  return list2
        if list2 is None:  return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2

    # -------- 迭代版本 --------
    def mergeTwoLists_iterative(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 将两个升序链表合并为一个新的升序链表
        方法: 迭代法, 使用哨兵节点
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

    # ========================================================
    #  LeetCode 206 · 反转链表
    # ========================================================
    # -------- 递归版本 --------
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 反转单链表
        方法: 递归到链表尾部后反转指针方向
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
        功能: 反转单链表
        方法: 迭代法, 双指针
        """
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    # --------------------------------------------------------
    #  LeetCode 876 · 链表的中间结点
    # --------------------------------------------------------
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 返回链表的中间节点；若有两个中间节点返回第二个
        技巧: 快慢指针
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # --------------------------------------------------------
    #  LeetCode 234 · 回文链表
    # --------------------------------------------------------
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        功能: 判断链表是否为回文
        方法: 找到中点, 反转后半部分, 然后比较
        """
        latter = self.reverseList_iterative(self.middleNode(head))
        while latter:
            if head.val != latter.val:
                return False
            head = head.next
            latter = latter.next
        return True

    # --------------------------------------------------------
    #  LeetCode 160 · 相交链表
    # --------------------------------------------------------
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        功能: 找到两个单链表相交的起始节点
        技巧: 双指针法
        """
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

    # --------------------------------------------------------
    #  LeetCode 141 · 环形链表
    # --------------------------------------------------------
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        功能: 判断链表中是否有环
        技巧: 快慢指针
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # --------------------------------------------------------
    #  LeetCode 142 · 环形链表 II
    # --------------------------------------------------------
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 返回链表入环的第一个节点；若无环返回 None
        原理: 相遇后再同步前进
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:            # 相遇
                while slow is not head: # 再走 a 步
                    slow = slow.next
                    head = head.next
                return slow
        return None

    # --------------------------------------------------------
    #  LeetCode 148 · 排序链表
    # --------------------------------------------------------
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 链表归并排序
        """
        if not head or not head.next:
            return head
            
        # 找中点, 断链
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

    # ========================================================
    #  LeetCode 24 · 两两交换链表中的节点
    # ========================================================
    # -------- 迭代版本 --------
    def swapPairs_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        功能: 两两交换链表中相邻的节点
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
        功能: 两两交换链表中相邻的节点
        """
        if head is None or head.next is None:
            return head
            
        node1 = head
        node2 = head.next
        node3 = node2.next
        
        node1.next = self.swapPairs_recursive(node3)
        node2.next = node1
        return node2

    # ========================================================
    #  LeetCode 23 · 合并 K 个升序链表
    # ========================================================
    # -------- 堆方法 --------
    def mergeKLists_heap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        功能: 最小堆, 时间复杂度 O(n log k)
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
    def mergeKLists_divideConquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        功能: 分治合并, 时间复杂度 O(n log k)
        """
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]
        left = self.mergeKLists_divideConquer(lists[:m // 2])
        right = self.mergeKLists_divideConquer(lists[m // 2:])
        return self.mergeTwoLists_iterative(left, right)
