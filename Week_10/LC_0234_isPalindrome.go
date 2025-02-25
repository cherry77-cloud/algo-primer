/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    slow, fast := head, head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }
    return slow
}

func reverseList(head *ListNode) *ListNode {
    var pre, cur *ListNode = nil, head
    for cur != nil {
        nxt := cur.Next
        cur.Next = pre
        pre = cur
        cur = nxt
    }
    return pre
}

func isPalindrome(head *ListNode) bool {
    mid := middleNode(head)
    head2 := reverseList(mid)
    for head2 != nil {
        if head.Val != head2.Val { // 不是回文链表
            return false
        }
        head = head.Next
        head2 = head2.Next
    }
    return true
}
