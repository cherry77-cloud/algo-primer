/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    pre := math.MinInt
    var dfs func(*TreeNode) bool 
    dfs = func(node *TreeNode) bool {
        if node == nil {
            return true
        }
        if !dfs(node.Left) || node.Val <= pre {
            return false
        }
        pre = node.Val
        return dfs(node.Right)
    }
    return dfs(root)
}
