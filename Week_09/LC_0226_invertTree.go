/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func invertTree(root *TreeNode) *TreeNode {
    if root == nil {
        return nil
    }
    root.Left, root.Right = root.Right, root.Left  // 交换左右儿子
    invertTree(root.Left)    // 翻转左子树
    invertTree(root.Right)   // 翻转右子树
    return root
}
