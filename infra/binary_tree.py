from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeTraversal:
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
        stack: List[TreeNode] = []   # 仅存放右子节点
        res: List[int] = []
        node = root
        while stack or node:
            while node:                    # 沿左链一路访问
                res.append(node.val)       # 访问根
                if node.right:             # 右子树留到之后处理
                    stack.append(node.right)
                node = node.left           # 转向左子树
            if stack:                      # 左侧到底，弹出下一个右子树根
                node = stack.pop()
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
        res: List[int] = []
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
        单栈后序遍历，左-右-根顺序
             1. 使用 prev 指针记录上一个访问的节点
             2. 一路向左压栈，到达最左节点
             3. 查看栈顶：如果无右孩子或右孩子已访问，则可以访问当前节点
             4. 否则需要先处理右子树，转向右孩子
             5. prev 指针确保每个节点只被访问一次
        """
        stack: List[TreeNode] = []
        res: List[int] = []
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

    # ░░░░░░░░░░░ LeetCode 144 —— Morris 前序遍历 ░░░░░░░░░░░
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris前序遍历，根-左-右顺序
            1. 利用空闲的右指针建立临时线索，实现无栈遍历
            2. 对每个节点找其左子树的最右节点（前驱）
            3. 第一次到达时：访问当前节点，建立线索，转向左子树
            4. 第二次到达时：说明左子树已遍历完，恢复结构，转向右子树
            5. 无左子树的节点直接访问后向右走
        """
        result: List[int] = []
        cur = root
        while cur:
            if cur.left is None:              # 无左子树，直接访问，然后向右走
                result.append(cur.val)
                cur = cur.right
            else:                             # 找左子树的最右节点（前驱）
                predecessor = cur.left
                while predecessor.right and predecessor.right is not cur:
                    predecessor = predecessor.right
                if predecessor.right is None: # 第一次到达前驱：建立线索并访问当前节点
                    result.append(cur.val)    # preorder 先访问根
                    predecessor.right = cur   # 线索化
                    cur = cur.left
                else:                         # 第二次到达前驱：恢复结构，转向右子树
                    predecessor.right = None
                    cur = cur.right
        return result

    # ░░░░░░░░░░░ LeetCode 94 —— Morris 中序遍历 ░░░░░░░░░░░
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris中序遍历，左-根-右顺序，
            1. 利用空闲的右指针建立临时线索，实现无栈遍历
            2. 对每个节点找其左子树的最右节点（前驱）
            3. 第一次到达时：建立线索，转向左子树（不访问）
            4. 第二次到达时：左子树已遍历完，访问当前节点，恢复结构，转向右子树
            5. 无左子树的节点说明是最左侧，直接访问后向右走
        """
        result: List[int] = []
        cur = root
        while cur:
            if cur.left is None:              # 无左子树，直接访问，然后向右走
                result.append(cur.val)
                cur = cur.right
            else:                             # 找左子树的最右节点（前驱）
                predecessor = cur.left
                while predecessor.right and predecessor.right is not cur:
                    predecessor = predecessor.right
                if predecessor.right is None: # 第一次到达前驱：建立线索，转向左子树
                    predecessor.right = cur
                    cur = cur.left
                else:                         # 第二次到达前驱：恢复结构并访问当前节点
                    predecessor.right = None
                    result.append(cur.val)    # inorder 在回溯时访问根
                    cur = cur.right
        return result

    # ░░░░░░░░░░░ LeetCode 145 —— Morris 后序遍历 ░░░░░░░░░░░
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Morris后序遍历，左-右-根顺序
             1. 对每个节点找其左子树的最右节点（前驱）
             2. 第二次到达前驱时：逆序添加从当前节点左孩子到前驱的路径
             3. 使用切片反转避免手动交换
             4. 最后处理从根到最右节点的路径
             5. 无需虚拟节点，直接处理原树
        """
        def add_path(node: TreeNode) -> None:
            """添加右边界路径（逆序）"""
            path = []
            while node:
                path.append(node.val)
                node = node.right
            result.extend(reversed(path))
    
        result: List[int] = []
        cur = root
        while cur:
            predecessor = cur.left
            if predecessor:                     # 有左子树
                while predecessor.right and predecessor.right is not cur:
                    predecessor = predecessor.right
                if not predecessor.right:       # 第一次到达
                    predecessor.right = cur
                    cur = cur.left
                else:                           # 第二次到达
                    predecessor.right = None
                    add_path(cur.left)
                    cur = cur.right
            else:                               # 无左子树
                cur = cur.right
    
        add_path(root)                          # 处理整棵树的右边界
        return result

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
        q: deque[TreeNode] = deque([root])
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


class BinaryTreeUtils
    # ░░░░░░░░░░░ LeetCode 100 —— 相同的树 ░░░░░░░░░░░
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        递归判断两棵二叉树是否相同
            1. 基本情况：如果有一个为空，判断两者是否都为空
            2. 如果都不为空，比较当前节点值是否相等
            3. 递归比较左子树是否相同
            4. 递归比较右子树是否相同
            5. 当前节点相同 = 值相等 且 左子树相同 且 右子树相同
        """
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    # ░░░░░░░░░░░ LeetCode 101 —— 对称二叉树 ░░░░░░░░░░░
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        判断二叉树是否对称（镜像）
            1. 定义递归函数 dfs(p, q) 检查两节点是否镜像
            2. 终止条件：若二者有一个为空，则判断二者是否都为空
            3. 若都非空，比较当前节点值是否相等
            4. 递归比较外侧子树 (p.left, q.right)
            5. 递归比较内侧子树 (p.right, q.left)
            6. 根节点对称 = 值相等 且 外侧对称 且 内侧对称
        """
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None or q is None:
                return p is q
            return p.val == q.val and dfs(p.left, q.right) and dfs(p.right, q.left)
            
        return dfs(root.left, root.right)

    # ░░░░░░░░░░░ LeetCode 104 —— 二叉树的最大深度 ░░░░░░░░░░░
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


class BinaryTreeDPEngine:
    # ░░░░░░░░░░░ LeetCode 543 —— 二叉树的直径 ░░░░░░░░░░░
    @staticmethod
    def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
        """
        计算二叉树的直径（最长路径的边数）
             1. 定义链长：从当前节点向下延伸的最大边数
             2. 空节点链长为 -1，叶子节点链长为 0
             3. 递归计算左右子树的最大链长
             4. 经过当前节点的最长路径 = 左链长 + 右链长 + 2
             5. 返回给父节点的链长 = max(左链长, 右链长) + 1
        """
        ans: int = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return -1  # 空节点链长为 -1
            l_len = dfs(node.left) + 1     # 左子树最大链长 + 1
            r_len = dfs(node.right) + 1    # 右子树最大链长 + 1
            nonlocal ans
            ans = max(ans, l_len + r_len)  # 更新全局最大直径
            return max(l_len, r_len)       # 返回当前子树最大链长
        dfs(root)
        return ans
