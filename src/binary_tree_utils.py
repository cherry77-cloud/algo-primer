from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeUtils:
    # ░░░░░░░░░░░ LeetCode 144 —— 二叉树前序遍历 ░░░░░░░░░░░
    @staticmethod
    def preorder(root: Optional[TreeNode]) -> List[int]:
        """根-左-右: 显式栈"""
        if not root:  return []
        stack: List[TreeNode] = [root]
        res:   List[int]      = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    # ░░░░░░░░░░░ LeetCode 94 —— 二叉树中序遍历 ░░░░░░░░░░░
    @staticmethod
    def inorder(root: Optional[TreeNode]) -> List[int]:
        """左-根-右: 显式栈遍历"""
        stack: List[TreeNode] = []
        res:   List[int]      = []
        node = root

        while stack or node:
            while node:                    # 不断向左下探
                stack.append(node)
                node = node.left
            node = stack.pop()             # 到达最左，开始回溯
            res.append(node.val)           # 访问根
            node = node.right              # 转向右子树
        return res
