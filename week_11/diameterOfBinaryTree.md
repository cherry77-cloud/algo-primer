```cpp
class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = INT_MIN;
        auto dfs = [&](this auto&& dfs, TreeNode* node) {
            if (node == nullptr) {
                return -1;
            }
            auto l_len = dfs(node->left) + 1;
            auto r_len = dfs(node->right) + 1;
            ans = max(ans, l_len + r_len);
            return max(l_len, r_len);
        };
        dfs(root);
        return ans;
    }
};
```

---

```go
func diameterOfBinaryTree(root *TreeNode) (ans int) {
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return -1
        }
        lLen := dfs(node.Left) + 1  // 左子树最大链长+1
        rLen := dfs(node.Right) + 1 // 右子树最大链长+1
        ans = max(ans, lLen+rLen)   // 两条链拼成路径
        return max(lLen, rLen)      // 当前子树最大链长
    }
    dfs(root)
    return
}
```
