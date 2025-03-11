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
