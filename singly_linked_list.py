class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
       """
       两数相加 - LeetCode 2
       功能：将两个链表表示的数字相加，每个节点存储一位数字（逆序存储）
       示例：l1 = [2,4,3] 表示 342
            l2 = [5,6,4] 表示 465
            结果 = [7,0,8] 表示 807 (342 + 465 = 807)
       """
       cur = dummy = ListNode()  # 哨兵节点
       carry = 0  # 进位
       while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
           if l1:
               carry += l1.val  # 节点值和进位加在一起
               l1 = l1.next  # 下一个节点
           if l2:
               carry += l2.val  # 节点值和进位加在一起
               l2 = l2.next  # 下一个节点
           cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
           carry //= 10  # 新的进位
           cur = cur.next  # 下一个节点
       return dummy.next  # 哨兵节点的下一个节点就是头节点
   
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       """
       删除链表的倒数第N个节点 - LeetCode 19
       功能：删除链表倒数第n个节点，并返回链表头节点
       示例：链表 = [1,2,3,4,5], n = 2
            结果 = [1,2,3,5] (删除了倒数第2个节点4)
       技巧：使用快慢指针，快指针先走n步，然后两指针同步移动
       """
       # 由于可能会删除链表头部，用哨兵节点简化代码
       left = right = dummy = ListNode(next=head)
       for _ in range(n):
           right = right.next  # 右指针先向右走 n 步
       while right.next:
           left = left.next
           right = right.next  # 左右指针一起走
       left.next = left.next.next  # 左指针的下一个节点就是倒数第 n 个节点
       return dummy.next
   
   def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       """
       合并两个有序链表 - LeetCode 21
       功能：将两个升序链表合并为一个新的升序链表
       示例：list1 = [1,2,4], list2 = [1,3,4]
            结果 = [1,1,2,3,4,4]
       方法：递归比较两个链表的头节点，选择较小的节点
       """
       # ---- 1. 终止条件：某个链表为空 ----
       # 只要有一个链表到头，另一个链表剩余部分直接接上
       if list1 is None:  return list2
       if list2 is None:  return list1
       # ---- 2. 递归主体：比较当前节点 ----
       if list1.val < list2.val:
           # list1 当前值更小：选它作为本层链表的头节点
           # 接着合并 list1 的剩余部分 list1.next 与 list2. 合并结果接到 list1.next 上
           list1.next = self.mergeTwoLists(list1.next, list2)
           return list1  # 返回排好序的头节点 list1
       else:
           list2.next = self.mergeTwoLists(list1, list2.next)
           return list2
   
   def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       """
       反转链表 - LeetCode 206
       功能：反转单链表
       示例：输入 = [1,2,3,4,5]
            输出 = [5,4,3,2,1]
       方法：递归到链表尾部，然后从后往前反转指针方向
       """
       # ---- 1. 终止条件 ----
       if head is None or head.next is None:
           return head  # 此时 head 就是最尾节点，作为 new_head 向上返回
       # ---- 2. 递归反转后续链表 ----
       new_head = self.reverseList(head.next)  # new_head 持有最终头结点，全程不变
       # ---- 3. 指针反向 ----
       head.next.next = head  # 把子链表尾巴指回当前节点
       # ---- 4. 断开旧链接 ----
       head.next = None       # 当前节点成为新的尾结点
       # ---- 5. 向上传递 new_head ----
       return new_head        # 不再修改，直接返回给上一层
