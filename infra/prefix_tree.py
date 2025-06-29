# ░░░░░░░░░░░░░░ LeetCode 208 - 实现 Trie (前缀树) ░░░░░░░░░░░░░░
class Trie:
    """ 前缀树实现 - 支持插入、完整搜索、前缀搜索. 使用 26 叉树存储小写字母，__slots__ 优化内存 """
    class TrieNode:
        __slots__ = ('son', 'is_end')  # 只声明实例会用到的两个属性，节省内存
        def __init__(self):
            self.son = [None] * 26  # son[i] 指向字符 chr(i + ord('a')) 对应的子节点
            self.is_end = False     # 标记该节点是否为某单词结尾

    def __init__(self):
        self.root = self.TrieNode()  # 初始化根节点

    def insert(self, word: str) -> None:
        """插入单词到前缀树"""
        node = self.root
        for char in word:
            index = ord(char) - ord('a')  # 将字符映射到 0~25 的数组下标
            if not node.son[index]:       # 若不存在该字符的子节点，则创建新节点
                node.son[index] = self.TrieNode()
            node = node.son[index]  # 继续向下遍历
        node.is_end = True  # 单词插入完毕，标记结尾

    def search(self, word: str) -> bool:
        """搜索完整单词是否存在"""
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.son[index]:
                return False  # 途中缺节点，说明单词不存在
            node = node.son[index]
        return node.is_end    # 只有走到结尾并且 is_end=True 才算找到

    def startsWith(self, prefix: str) -> bool:
        """搜索是否存在以 prefix 为前缀的单词"""
        node = self.root
        for char in prefix:
            index = ord(char) - ord('a')
            if not node.son[index]:
                return False  # 前缀路径不存在
            node = node.son[index]
        return True           # 只要顺利遍历完前缀即表示存在该前缀


# ░░░░░░░░░░░░░░ LeetCode 421 - 数组中两个数的最大异或值 ░░░░░░░░░░░░░░
class XORTrie:
    class TrieNode:
        def __init__(self):
            self.children = [None, None]

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, num: int) -> None:
        """把整数 num 按二进制插入字典树"""
        node = self.root
        for i in range(31, -1, -1):       # 处理 32 位非负整数
            bit = (num >> i) & 1
            if not node.children[bit]:
                node.children[bit] = self.TrieNode()
            node = node.children[bit]

    def query(self, num: int) -> int:
        """返回 num 与树中任意数的最大异或值"""
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled = 1 - bit        # 希望走相反的位以增大异或值
            if node.children[toggled]:
                max_xor |= (1 << i)
                node = node.children[toggled]
            else:
                node = node.children[bit]
        return max_xor
