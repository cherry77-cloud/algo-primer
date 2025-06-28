class TrieToolkit:
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
