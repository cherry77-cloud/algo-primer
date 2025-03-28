```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy;
        auto cur = &dummy;
        while (l1 && l2) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
            } else {
                cur->next = l2;
                l2 = l2->next;
            }
            cur = cur->next;
        }
        cur->next = l1 == nullptr ? l2 : l1;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists, int i, int j) {
        int m = j - i;
        if (m == 0)  return nullptr;
        if (m == 1)  return lists[i];
        auto left = mergeKLists(lists, i, i + m / 2);
        auto right = mergeKLists(lists, i + m / 2, j);
        return mergeTwoLists(left, right);
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        return mergeKLists(lists, 0, lists.size());
    }
};
```

---

```go
func mergeKLists(lists []*ListNode) *ListNode {
    h := hp{}
    for _, head := range lists {
        if head != nil {
            h = append(h, head)
        }
    }
    heap.Init(&h)

    dummy := &ListNode{}
    cur := dummy
    for len(h) > 0 {
        node := heap.Pop(&h).(*ListNode)
        if node.Next != nil {
            heap.Push(&h, node.Next)
        }
        cur.Next = node
        cur = cur.Next
    }
    return dummy.Next
}

type hp []*ListNode

func (h hp) Len() int {
    return len(h)
}

func (h hp) Less(i, j int) bool {
    return h[i].Val < h[j].Val
}

func (h hp) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h *hp) Push(v any) {
    *h = append(*h, v.(*ListNode))
}

func (h *hp) Pop() any {
    a := *h
    v := a[len(a) - 1]
    *h = a[:len(a) - 1]
    return v
}
```
