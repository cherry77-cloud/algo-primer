/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    slow, fast := head, head     // 乌龟和兔子同时从起点出发
    for fast != nil && fast.Next != nil {
        slow = slow.Next         // 乌龟走一步
        fast = fast.Next.Next    // 兔子走两步
        if slow == fast {        // 兔子追上乌龟（套圈），说明有环
            return true
        }
    }
    return false                 // 访问到了链表末尾，无环
}
