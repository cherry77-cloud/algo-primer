/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return nil
    }
    ans := [][]int{}
    q := []*TreeNode{root}
    for len(q) > 0 {
        n := len(q)
        vals := make([]int, n)
        for i := range vals {
            node := q[0]
            q = q[1:]
            vals[i] = node.Val
            if node.Left != nil {
                q = append(q, node.Left)
            }
            if node.Right != nil {
                q = append(q, node.Right)
            }
        }
        ans = append(ans, vals)
    }
    return ans
}
