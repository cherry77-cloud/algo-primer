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

    # ░░░░░░░░░░░ LeetCode 145 —— 二叉树后序遍历 ░░░░░░░░░░░
    @staticmethod
    def postorder(root: Optional[TreeNode]) -> List[int]:
        """左-右-根；双栈反序输出"""
        if not root:  return []
        stack1: List[TreeNode] = [root]
        stack2: List[TreeNode] = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return [node.val for node in reversed(stack2)

    # ░░░░░░░░░░░ LeetCode 145 —— 二叉树后序遍历（单栈版） ░░░░░░░░░░░
    @staticmethod
    def postorder(root: Optional[TreeNode]) -> List[int]:
        """左-右-根；单栈 + prev 指针"""
        if not root:  return []
        stack: List[TreeNode] = []
        res:   List[int]      = []
        node, prev = root, None
        while stack or node:
            while node:                      # 一路压左孩子
                stack.append(node)
                node = node.left
            node = stack[-1]                 # 查看栈顶
            if not node.right or node.right is prev:
                stack.pop()
                res.append(node.val)         # 访问根
                prev = node                  # 记录已访问
                node = None                  # 回溯继续
            else:
                node = node.right            # 转向右子树
        return res

    # ░░░░░░░░░░░ LeetCode 102 —— 二叉树层序遍历 ░░░░░░░░░░░
    @staticmethod
    def level_order(root: Optional[TreeNode]) -> List[List[int]]:
        """按层收集节点；队列 BFS"""
        if not root:  return []
        q: deque[TreeNode]   = deque([root])
        res: List[List[int]] = []
        while q:
            level_size = len(q)
            level_vals: List[int] = []
            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level_vals)
        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """计算二叉树最大深度"""
        if not root:  return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return max(l_depth, r_depth) + 1
