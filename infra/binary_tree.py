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
        """
        迭代前序遍历，根-左-右顺序
             1. 使用栈模拟递归过程，根节点入栈
             2. 弹出栈顶节点，访问其值（根）
             3. 先将右孩子入栈，再将左孩子入栈（栈是后进先出）
             4. 这样保证左孩子先被处理，符合根-左-右顺序
             5. 重复直到栈为空，遍历完成
        """
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
        """
        迭代中序遍历，左-根-右顺序
             1. 使用栈和指针配合，先一路向左走到底
             2. 将沿途节点都压入栈中（保存回溯路径）
             3. 到达最左节点后，弹栈并访问（此时是左子树最左节点）
             4. 访问完节点后，转向其右子树
             5. 重复过程，实现左-根-右的访问顺序
        """
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
        """
        双栈后序遍历，左-右-根顺序
             1. 第一个栈用于遍历，第二个栈用于反序
             2. 类似前序遍历，但先压左孩子，再压右孩子
             3. 这样得到根-右-左的访问顺序
             4. 将访问的节点压入第二个栈
             5. 最后反序输出第二个栈，得到左-右-根
        """
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

    # ░░░░░░░░░░░ LeetCode 145 —— 二叉树后序遍历 ░░░░░░░░░░░
    @staticmethod
    def postorder(root: Optional[TreeNode]) -> List[int]:
        """
        单栈后序遍历，左-右-根顺序
             1. 使用 prev 指针记录上一个访问的节点
             2. 一路向左压栈，到达最左节点
             3. 查看栈顶：如果无右孩子或右孩子已访问，则可以访问当前节点
             4. 否则需要先处理右子树，转向右孩子
             5. prev 指针确保每个节点只被访问一次
        """
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
        """
        BFS 层序遍历，逐层访问节点
             1. 使用队列存储当前层的所有节点
             2. 记录当前层的节点个数（队列当前大小）
             3. 处理当前层所有节点，收集它们的值
             4. 将每个节点的左右孩子加入队列（下一层）
             5. 每层的值作为一个列表，最终返回二维列表
        """
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
        """
        递归计算二叉树最大深度
             1. 基本情况：空节点深度为 0
             2. 递归计算左子树的最大深度
             3. 递归计算右子树的最大深度
             4. 当前节点的深度 = max(左深度, 右深度) + 1
             5. 返回根节点的深度即为整棵树的最大深度
        """
        if not root:  return 0
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return max(l_depth, r_depth) + 1
