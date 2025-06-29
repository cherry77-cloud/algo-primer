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


# ░░░░░░░░░░░░░░ AcWing 142 - 前缀统计 ░░░░░░░░░░░░░░
class TriePrefixCounter:
    """
    前缀统计 - 统计以某个字符串为前缀的单词数量
    1. 将所有字符串插入 Trie 树
    2. 在每个单词结尾节点记录出现次数
    3. 查询时累加路径上所有结尾节点的计数
    """
    class TrieNode:
        __slots__ = ("children", "count")
        def __init__(self) -> None:
            self.children = {}
            self.count: int = 0

    def __init__(self) -> None:
        """初始化根节点"""
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        """将单词插入 Trie 树，并在结尾节点累加计数"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.count += 1

    def query(self, prefix: str) -> int:
        """ 查询有多少个单词以 prefix 为前缀: 累加从根到 prefix 路径上各节点的 count 值 """
        node = self.root
        total = 0
        for char in prefix:
            if char not in node.children:
                return total
            node = node.children[char]
            total += node.count
        return total


# ░░░░░░░░░░░░░░ AcWing 835 - Trie 字符串统计 ░░░░░░░░░░░░░░
class TrieWithCount:
    """带计数功能的前缀树 - 统计每个字符串出现的次数. 使用字典存储子节点，支持任意字符"""
    class TrieNode:
        __slots__ = ('children', 'count')
        def __init__(self) -> None:
            self.children: dict[str, "TrieWithCount.TrieNode"] = {}   # children: 键为字符，值为 TrieNode 实例
            self.count: int = 0

    def __init__(self) -> None:
        self.root = self.TrieNode()

    def insert(self, word: str) -> None:
        """插入字符串，如果已存在则计数加一"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.TrieNode()
            node = node.children[char]
        node.count += 1

    def query(self, word: str) -> int:
        """查询字符串出现的次数"""
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return 0
        return node.count


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


# ░░░░░░░░░░░░░░ AcWing 144 - 树上最大异或路径 ░░░░░░░░░░░░░░
class TreeMaxXorPath:
    """
    树上最大异或路径问题: 给定一棵 n 个节点的树，每条边有权值 w[i]. 求树上任意两点路径的最大异或值
    
    1. DFS 计算每个节点到根的异或距离
      - 定义 dist[u] = 从根节点到 u 的路径上所有边权的异或值
      - 通过 DFS 遍历，dist[v] = dist[u] ^ w(u,v)
   
    2. 两点间路径的异或值 = dist[u] ^ dist[v]（LCA性质）
       证明：设 u, v 的最近公共祖先为 lca
       - u 到 v 的路径 = (u → lca) + (lca → v)
       - dist[u] = (root → lca) ^ (lca → u)
       - dist[v] = (root → lca) ^ (lca → v)
       - dist[u] ^ dist[v] = (root → lca) ^ (lca → u) ^ (root → lca) ^ (lca → v)
                           = (lca → u) ^ (lca → v)  [root → lca 异或两次抵消]
                           = u 到 v 路径的异或值
    3. 问题转化为：在 dist 数组中找两个数使其异或值最大
       - 原问题：max{path_xor(u,v)} for all u,v
       - 转化后：max{dist[i] ^ dist[j]} for all i,j
       - 使用贪心+哈希的方法解决最大异或对问题
    """
    @staticmethod
    def findMaximumXOR(nums: List[int]) -> int:
        """LeetCode 421: 位掩码 + 哈希集合 求数组最大异或对"""
        ans = mask = 0
        high_bit = max(nums).bit_length() - 1
        for i in range(high_bit, -1, -1):
            mask |= 1 << i
            candidate = ans | (1 << i)
            seen = set()
            for x in nums:
                x &= mask
                if candidate ^ x in seen:
                    ans = candidate
                    break
                seen.add(x)
        return ans

    def __init__(self) -> None:
        self.graph: DefaultDict[int, List[Tuple[int, int]]] = defaultdict(list)
        self.dist: Dict[int, int] = {}
        self.vis: Set[int] = set()

    def add_edge(self, u: int, v: int, w: int) -> None:
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dfs(self, u: int, xor_dist: int = 0) -> None:
        self.vis.add(u)
        self.dist[u] = xor_dist
        for v, w in self.graph[u]:
            if v not in self.vis:
                self.dfs(v, xor_dist ^ w)

    def solve(self, n: int, edges: List[Tuple[int, int, int]]) -> int:
        """返回树上最大异或路径值"""
        for u, v, w in edges:
            self.add_edge(u, v, w)
        self.dfs(0)
        arr = [self.dist[i] for i in range(n)]
        return self.findMaximumXOR(arr)
