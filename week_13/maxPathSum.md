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
    int maxPathSum(TreeNode* root) {
        int ans = INT_MIN;
        auto dfs = [&](this auto&& dfs, TreeNode* node) -> int {
            if (node == nullptr) {
                return 0;  // 虚拟节点，和为0
            }
            int l_sum = dfs(node->left);   // 左子树最大链和
            int r_sum = dfs(node->right);  // 右子树最大链和
            ans = max(ans, l_sum + r_sum + node->val);     // 两条链拼成路径
            return max(max(l_sum, r_sum) + node->val, 0);  // 当前子树最大链和
        };
        dfs(root);
        return ans;
    }
};
```
