/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sortedArrayToBST(nums []int) *TreeNode {
    if len(nums) == 0 {
        return nil
    }
    m := len(nums) / 2
    return &TreeNode {
        Val: nums[m],
        Left: sortedArrayToBST(nums[:m]),
        Right: sortedArrayToBST(nums[m + 1:]),
    }
}
