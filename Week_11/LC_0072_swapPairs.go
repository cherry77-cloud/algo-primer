/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head} // 用哨兵节点简化代码逻辑
    node0 := dummy
    node1 := head
    for node1 != nil && node1.Next != nil { // 至少有两个节点
        node2 := node1.Next
        node3 := node2.Next

        node0.Next = node2 // 0 -> 2
        node2.Next = node1 // 2 -> 1
        node1.Next = node3 // 1 -> 3

        node0 = node1 // 下一轮交换，0 是 1
        node1 = node3 // 下一轮交换，1 是 3
    }
    return dummy.Next // 返回新链表的头节点
}
