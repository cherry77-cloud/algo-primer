/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSameTree(p, q *TreeNode) bool {
    if p == nil || q == nil {
        return p == q
    }
    return p.Val == q.Val && isSameTree(p.Left, q.Right) && isSameTree(p.Right, q.Left)
}


func isSymmetric(root *TreeNode) bool {
    return isSameTree(root.Left, root.Right)    
}
