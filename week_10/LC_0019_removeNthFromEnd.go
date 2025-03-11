/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    // 由于可能会删除链表头部，用哨兵节点简化代码
    dummy := &ListNode{Next: head}
    left, right := dummy, dummy
    for ; n > 0; n-- {
        right = right.Next // 右指针先向右走 n 步
    }
    for right.Next != nil {
        left = left.Next
        right = right.Next // 左右指针一起走
    }
    left.Next = left.Next.Next // 左指针的下一个节点就是倒数第 n 个节点
    return dummy.Next
}
