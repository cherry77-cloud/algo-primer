```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        ListNode* cur = &dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            if (l1) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2) {
                carry += l2->val;
                l2 = l2->next;
            }
            cur = cur->next = new ListNode(carry % 10);
            carry /= 10;
        }
        return dummy.next;
    }
};
```

---

```go
func addTwoNumbers(l1, l2 *ListNode) *ListNode {
    dummy := ListNode{} // 哨兵节点
    cur := &dummy
    carry := 0 // 进位
    for l1 != nil || l2 != nil || carry != 0 { // 有一个不是空节点，或者还有进位，就继续迭代
        if l1 != nil {
            carry += l1.Val // 节点值和进位加在一起
            l1 = l1.Next // 下一个节点
        }
        if l2 != nil {
            carry += l2.Val // 节点值和进位加在一起
            l2 = l2.Next // 下一个节点
        }
        cur.Next = &ListNode{Val: carry % 10} // 每个节点保存一个数位
        carry /= 10 // 新的进位
        cur = cur.Next // 下一个节点
    }
    return dummy.Next // 哨兵节点的下一个节点就是头节点
}
```
