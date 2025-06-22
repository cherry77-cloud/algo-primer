from typing import List, Optional
import heapq
from heapq import heapify, heappush, heappop


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        两数相加 - LeetCode 2
        功能：将两个链表表示的数字相加，每个节点存储一位数字（逆序存储）
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        删除链表的倒数第N个节点 - LeetCode 19
        功能: 删除链表倒数第n个节点, 并返回链表头节点
        技巧:使用快慢指针, 快指针先走n步, 然后两指针同步移动
        """
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表 - LeetCode 21 (递归版本)
        功能: 将两个升序链表合并为一个新的升序链表
        方法: 递归比较两个链表的头节点, 选择较小的节点
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoListsRecursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoListsRecursive(list1, list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        合并两个有序链表 - LeetCode 21 (迭代版本)
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
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表 - LeetCode 206 (递归版本)
        功能: 反转单链表
        方法: 递归到链表尾部, 然后从后往前反转指针方向
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        反转链表 - LeetCode 206 (迭代版本)
        功能: 反转单链表
        方法: 迭代法, 双指针
        """
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre     # 反转指向
            pre = cur          # pre 前进
            cur = nxt          # cur 前进
        return pre

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        链表的中间结点 - LeetCode 876
        功能: 返回链表的中间节点, 如果有两个中间节点, 返回第二个
        技巧: 快慢指针, 快指针走两步, 慢指针走一步
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        回文链表 - LeetCode 234
        功能: 判断链表是否是回文链表
        方法: 找到中点, 反转后半部分, 然后比较
        """
        latter = self.reverseList(self.middleNode(head))
        while latter:
            if head.val != latter.val:
                return False
            head = head.next
            latter = latter.next
        return True

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        相交链表 - LeetCode 160
        功能: 找到两个单链表相交的起始节点
        技巧: 双指针法, 当一个指针到达尾部时切换到另一个链表头部
        """
        p, q = headA, headB
        while p is not q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        环形链表 - LeetCode 141
        功能: 判断链表中是否有环
        技巧: 快慢指针, 如果有环, 快指针最终会追上慢指针
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        环形链表 II - LeetCode 142
        功能: 返回链表开始入环的第一个节点, 如果无环返回 None
        原理: 快慢指针相遇后, 从头节点和相遇点同时出发, 再次相遇点即为环入口
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        排序链表 - LeetCode 148
        方法: 归并排序, 使用快慢指针找中点
        """
        if not head or not head.next:
            return head
        
        # 找中点并断链 - 使用快慢指针，需要记录慢指针的前一个节点
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.mergeTwoLists(left, right)

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        两两交换链表中的节点 - LeetCode 24
        功能: 两两交换链表中相邻的节点
        """
        node0 = dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        node1 = head
        while node1 and node1.next:  # 至少有两个节点
            node2 = node1.next
            node3 = node2.next

            node0.next = node2  # 0 -> 2
            node2.next = node1  # 2 -> 1
            node1.next = node3  # 1 -> 3

            node0 = node1  # 下一轮交换，0 是 1
            node1 = node3  # 下一轮交换，1 是 3
        return dummy.next  # 返回新链表的头节点

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        两两交换链表中的节点 - LeetCode 24
        功能: 两两交换链表中相邻的节点
        """
        if head is None or head.next is None:  # 递归边界
            return head  # 不足两个节点, 无需交换
            
        node1 = head
        node2 = head.next
        node3 = node2.next
        
        node1.next = self.swapPairsRecursive(node3)  # 1 指向递归返回的链表头
        node2.next = node1  # 2 指向 1
        return node2  # 返回交换后的链表头节点

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合并K个升序链表 - LeetCode 23 (堆方法)
        功能: 合并k个已排序的链表。最小堆，时间复杂度 O(nlogk)
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
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        合并K个升序链表 - LeetCode 23 (分治法)
        功能: 合并k个已排序的链表。分治法, 时间复杂度 O(nlogk)
        """
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]
        left = self.mergeKLists(lists[:m//2])
        right = self.mergeKLists(lists[m//2:])
        return self.mergeTwoLists(left, right)
