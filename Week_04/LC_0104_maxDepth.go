/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
    // 自底向上
    if root == nil {
        return 0
    }
    lDepth := maxDepth(root.Left)
    rDepth := maxDepth(root.Right)
    return max(lDepth, rDepth) + 1
}
