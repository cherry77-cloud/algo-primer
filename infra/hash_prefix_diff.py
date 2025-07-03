from collections import defaultdict
from typing import List, Dict


class HashTableUtils:
    # ░░░░░░░░░░░ LeetCode 49 —— 字母异位词分组 ░░░░░░░░░░░
    @staticmethod
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        """
        哈希表分组，排序字符作为键
             1. 创建哈希表，键为排序后的字符元组，值为原字符串列表
             2. 遍历每个字符串，将其字符排序得到唯一标识
             3. 字母异位词排序后相同，会映射到同一个键
             4. 将原字符串添加到对应键的列表中
             5. 返回哈希表中所有值的列表，即分组结果
        """
        hashtable: Dict[tuple, List[str]] = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            hashtable[key].append(s)
        return list(hashtable.values())

    # ░░░░░░░░░░░ LeetCode 128 —— 最长连续序列 ░░░░░░░░░░░
    @staticmethod
    def longestConsecutive(nums: List[int]) -> int:
        """
        哈希集合 + 贪心搜索最长序列
             1. 将所有数字放入哈希集合，实现 O(1) 查找
             2. 遍历集合中每个数字，判断是否为序列起点
             3. 如果 x-1 存在，说明 x 不是起点，跳过
             4. 从起点开始，不断查找 x+1, x+2... 直到断开
             5. 记录最长序列长度，时间复杂度 O(n)
        """
        seen = set(nums)
        longest = 0
        for x in seen:
            if x - 1 in seen:
                continue
            y = x
            while y in seen:
                y += 1
            longest = max(longest, y - x)
        return longest

    # ░░░░░░░░░░░ LeetCode 560 —— 和为 K 的子数组 ░░░░░░░░░░░
    @staticmethod
    def subarraySum(nums: List[int], k: int) -> int:
        """
        前缀和 + 哈希表计数
             1. 维护前缀和 pre_s 和哈希表 cnt 记录前缀和出现次数
             2. 对于位置 i，先将当前前缀和计入哈希表
             3. 更新前缀和：pre_s += nums[i]
             4. 查找满足 pre_s - (pre_s - k) = k 的子数组个数
             5. 即查找哈希表中 pre_s - k 出现的次数
        """
        cnt: Dict[int, int] = defaultdict(int)
        pre_s: int = 0
        ans: int = 0
        for x in nums:
            cnt[pre_s] += 1          # 记录当前前缀和出现次数
            pre_s += x
            ans += cnt[pre_s - k]    # 查找是否存在前缀和 pre_s - k
        return ans


# ░░░░░░░░░░░░░░ LeetCode 303 —— 区域和检索 - 数组不可变 ░░░░░░░░░░░░░░
class NumArray:
    """
    一维前缀和 - 支持O(1)查询区间和
        前缀和定义：s[i] = nums[0] + nums[1] + ... + nums[i-1]
        区间和查询：sumRange(left, right) = s[right+1] - s[left]
    """
    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s
    
    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


# ░░░░░░░░░░░░░░ LeetCode 304 —— 二维区域和检索 - 矩阵不可变 ░░░░░░░░░░░░░░
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        """
        前缀和定义：s[i][j] 表示从左上角 (0,0) 到右下角 (i-1,j-1) 的矩形区域和
        递推公式（容斥原理）：
            s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + matrix[i-1][j-1]
        """
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + matrix[i][j]
        self.s = s
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """
        查询从 (r1,c1) 到 (r2,c2) 的矩形区域和
        区域和 = s[r2+1][c2+1] - s[r2+1][c1] - s[r1][c2+1] + s[r1][c1]
        
        图示（查询区域用 * 标记）：
        +-------+-------+
        |   A   |   B   |
        +-------+-------+
        |   C   |  ***  |
        +-------+-------+
        
        区域和 = (A + B + C + *) - (A+C) - (A+B) + A = *
        """
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]


class PrefixDiffToolkit:
    # ░░░░░░░░░░░░░░ LeetCode 1094 —— 拼车 ░░░░░░░░░░░░░░
    @staticmethod
    def carPooling(trips: List[List[int]], capacity: int) -> bool:
        """
        差分数组应用 - 区间加减操作
            差分数组定义：diff[i] = nums[i] - nums[i-1]
            区间[l,r]加val：diff[l] += val, diff[r+1] -= val
            还原：nums[i] = diff[0] + diff[1] + ... + diff[i]
        """
        diff = [0] * 1001
        for num_passengers, from_loc, to_loc in trips:
            diff[from_loc] += num_passengers      # 上车
            diff[to_loc] -= num_passengers        # 下车
        return all(passengers <= capacity for passengers in accumulate(diff))
