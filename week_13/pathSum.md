```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        int ans = 0;
        unordered_map<long long, int> cnt{{0, 1}};
        auto dfs = [&](this auto&& dfs, TreeNode* node, long long s) {
            if (node == nullptr) {
                return;
            }
            s += node->val;
            ans += cnt.contains(s - targetSum) ? cnt[s-targetSum] : 0;
            cnt[s] += 1;
            dfs(node->left, s);
            dfs(node->right, s);
            // 因为去掉的是当前节点的信息 -> 从根到当前节点 node 的元素和
            cnt[s] -= 1;
        };
        dfs(root, 0);
        return ans;
    }
};
```

---

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pathSum(root *TreeNode, targetSum int) int {
    ans := 0
    cnt := map[int]int{0: 1}
    var dfs func(*TreeNode, int)
    dfs = func(node* TreeNode, s int) {
        if node == nil {
            return
        }
        s += node.Val
        ans += cnt[s - targetSum]
        cnt[s]++
        dfs(node.Left, s)
        dfs(node.Right, s)
        cnt[s]--
    }
    dfs(root, 0)
    return ans
}
```
