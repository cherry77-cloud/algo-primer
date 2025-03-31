```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy;
        auto cur = &dummy;
        while (list1 && list2) {
            if (list1->val <= list2->val) {
                cur->next = list1;
                list1 = list1->next;
            } else {
                cur->next = list2;
                list2 = list2->next;
            }
            cur = cur->next;
        }
        cur->next = list1 == nullptr ? list2 : list1;
        return dummy.next;
    }
};
```

---

```go
func mergeTwoLists(list1, list2 *ListNode) *ListNode {
    dummy := ListNode{} // 用哨兵节点简化代码逻辑
    cur := &dummy // cur 指向新链表的末尾
    for list1 != nil && list2 != nil {
        if list1.Val < list2.Val {
            cur.Next = list1 // 把 list1 加到新链表中
            list1 = list1.Next
        } else { // 注：相等的情况加哪个节点都是可以的
            cur.Next = list2 // 把 list2 加到新链表中
            list2 = list2.Next
        }
        cur = cur.Next
    }
    // 拼接剩余链表
    if list1 != nil {
        cur.Next = list1
    } else {
        cur.Next = list2
    }
    return dummy.Next
}
```
