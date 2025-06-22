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
       功能：删除链表倒数第n个节点，并返回链表头节点
       技巧：使用快慢指针，快指针先走n步，然后两指针同步移动
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
       合并两个有序链表 - LeetCode 21
       功能：将两个升序链表合并为一个新的升序链表
       方法：递归比较两个链表的头节点，选择较小的节点
       """
       if list1 is None:  return list2
       if list2 is None:  return list1
       if list1.val < list2.val:
           list1.next = self.mergeTwoLists(list1.next, list2)
           return list1
       else:
           list2.next = self.mergeTwoLists(list1, list2.next)
           return list2
   
   def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       """
       反转链表 - LeetCode 206
       功能：反转单链表
       方法：递归到链表尾部，然后从后往前反转指针方向
       """
       if head is None or head.next is None:
           return head
       new_head = self.reverseList(head.next)
       head.next.next = head
       head.next = None
       return new_head
