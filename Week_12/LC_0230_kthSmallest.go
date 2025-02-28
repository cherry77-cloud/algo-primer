func kthSmallest(root *TreeNode, k int) int {
    var dfs func(*TreeNode) int
    dfs = func(node *TreeNode) int {
        if node == nil {
            return -1 // 题目保证节点值非负，用 -1 表示没有找到
        }
        leftRes := dfs(node.Left)
        if leftRes != -1 { // 答案在左子树中
            return leftRes
        }
        k--
        if k == 0 { // 答案就是当前节点
            return node.Val
        }
        return dfs(node.Right) // 右子树会返回答案或者 -1
    }
    return dfs(root)
}
