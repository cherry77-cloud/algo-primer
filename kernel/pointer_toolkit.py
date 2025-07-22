class SlidingWindowUtils:
    # ░░░░░░░░░░░ LeetCode 3 —— 无重复字符的最长子串 ░░░░░░░░░░░
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        """
        不定长滑动窗口: 返回无重复字符的最长子串长度
            1. 使用滑动窗口维护一个无重复字符的子串
            2. 右指针不断扩展，将字符加入窗口
            3. 当出现重复字符时，收缩左边界直到窗口内无重复
            4. 记录过程中的最大窗口长度
        """
        ans = left = 0
        cnt = defaultdict(int)
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    # ░░░░░░░░░░░ LeetCode 135 —— 分发糖果 ░░░░░░░░░░░
    @staticmethod
    def candy(ratings: List[int]) -> int:
        """
        分发糖果问题
            1. 从左到右遍历，保证右边评分高的孩子比左边的多
            2. 从右到左遍历，保证左边评分高的孩子比右边的多
        """
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
                
        ans = 0
        for l, r in zip(left, right):
            ans += max(l, r)
        return ans

    # ░░░░░░░░░░░ LeetCode 438 · 找到字符串中所有字母异位词 ░░░░░░░░░░░
    @staticmethod
    def findAnagrams(s: str, p: str) -> List[int]:
        """
        定长滑动窗口: 返回字符串 s 中所有 p 的字母异位词起始索引
            1. 使用计数器记录目标串 p 中每个字符的需求量
            2. 滑动窗口遍历 s，右边界字符进入时减少需求
            3. 当某字符超量 cnt[c] < 0 时，收缩左边界
            4. 当窗口大小等于 p 的长度时，说明找到一个异位词
        """
        ans = []
        left = 0
        cnt = Counter(p)
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)         
        return ans
    
    # ░░░░░░░░░░░ LeetCode 76 · 最小覆盖子串 ░░░░░░░░░░░
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        """
        不定长滑动窗口: 找包含 t 所有字符的最小子串
            1. 使用计数器记录目标串 t 中每个字符的需求量
            2. less 变量记录还有几种字符未满足需求
            3. 右指针扩展窗口，当所有字符都满足时 less==0
            4. 收缩左边界找最小窗口，直到不再满足条件
            5. 记录过程中的最小窗口
        """
        ans_left, ans_right = -1, len(s)
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        
        less: int = len(cnt)
        left: int = 0
        
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while left <= right and less == 0:
                if right - left < ans_right - ans_left:
                    ans_right, ans_left = right, left
                if cnt[s[left]] == 0:
                    less += 1
                cnt[s[left]] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


class PrefixSuffixUtils:
    # ░░░░░░░░░░░ LeetCode 238 —— 除自身以外数组的乘积 ░░░░░░░░░░░
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        """
        计算除自身以外数组的乘积（不使用除法）
             1. 前缀积：pre[i] = nums[0] * nums[1] * ... * nums[i-1]
             2. 后缀积：suf[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
             3. 结果：result[i] = pre[i] * suf[i]
        """
        n = len(nums)
        pre = [1] * n
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
            
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        return [p * s for p, s in zip(pre, suf)]
        
    # ░░░░░░░░░░░ LeetCode 42 —— 接雨水 ░░░░░░░░░░░
    @staticmethod
    def trap(height: List[int]) -> int:
        """
        相向双指针+前后缀分解: 计算能接的雨水总量
            1. 雨水量取决于左右两侧的最高柱子中较矮的那个
            2. 使用双指针从两端向中间移动
            3. 维护左侧最高 pre_max 和右侧最高 suf_max
            4. 每次移动较矮一侧的指针，因为该侧的水量已确定
            5. 水量 = min(左侧最高, 右侧最高) - 当前高度
        """
        ans = pre_max = suf_max = 0
        left, right = 0, len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans

    # ░░░░░░░░░░░ LeetCode 11 —— 盛最多水的容器 ░░░░░░░░░░░
    @staticmethod
    def maxArea(height: List[int]) -> int:
        """
        相向双指针: 找两条线形成的最大面积
            1. 容器面积 = 宽度 × 高度 = (right-left) × min(h[left], h[right])
            2. 双指针从两端开始，初始宽度最大
            3. 每次移动较矮的那一端，因为：
               - 移动较高端：宽度减小，高度不增，面积必减小
               - 移动较矮端：宽度减小，但高度可能增加，面积可能增大
            4. 记录过程中的最大面积
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)
        return max_area

    # ░░░░░░░░░░░ LeetCode 15 —— 三数之和 ░░░░░░░░░░░
    @staticmethod
    def threeSum(nums: List[int]) -> List[List[int]]:
        """
        排序+相向双指针: 找所有和为 0 的三元组
            1. 先排序，方便去重和使用双指针
            2. 固定第一个数，用双指针在剩余部分找两数之和
            3. 去重技巧: 
               - 跳过重复的第一个数
               - 找到答案后跳过重复的第二、三个数
            4. 剪枝优化: 
               - 最小三数之和 > 0，后面不可能有解
               - 当前数与最大两数之和 < 0，跳过当前数
        """
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return ans


class PointerParadigms:
    # ░░░░░░░░░░░ LeetCode 5 —— 最长回文子串 ░░░░░░░░░░░
    @staticmethod
    def longestPalindrome(s: str) -> str:
        """
        中心扩展法: 以每个字符 / 字符间隙为中心向两侧扩张, 找到最长回文
            1. 回文定义 → 左右字符对称相等
            2. 枚举两类中心:
               • 奇数中心: (i, i)
               • 偶数中心: (i, i+1)
            3. 扩张条件: 0 ≤ left < right < n 且 s[left] == s[right]
            4. 记录并更新最长区间 [start, end]
        """
        def expandAroundCenter(left: int, right: int) -> Tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left  -= 1
                right += 1
            return left + 1, right - 1      # 回到合法边界

        start, end = 0, 0
        for i in range(len(s)):
            odd_left,  odd_right  = expandAroundCenter(i, i)
            even_left, event_right = expandAroundCenter(i, i + 1)
            if odd_right - odd_left > end - start:
                start, end = odd_left, odd_right
            if event_right - even_left > end - start:
                start, end = even_left, event_right
        return s[start : end + 1]

    # ░░░░░░░░░░░ LeetCode 287 —— 寻找重复数 ░░░░░░░░░░░
    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        """
        Floyd 环检测算法（快慢指针）
            1. 将数组下标视为链表结点，下标 i 指向 nums[i]
            2. 由于存在重复数，链表必定形成环
            3. 使用快慢指针找到环中相遇点
            4. 从头结点和相遇点同步前进，相遇处即为环的入口（即重复数）
        """
        def next(i: int) -> int:
            """返回下一个结点，链表指针由 nums[i] 决定"""
            return nums[i]
    
        slow = fast = 0
        while True:
            slow = next(slow)
            fast = next(next(fast))
            if slow == fast:
                break
    
        head = 0
        while head != slow:
            slow = next(slow)
            head = next(head)
        return slow

    # ░░░░░░░░░░░ LeetCode 189 —— 轮转数组 ░░░░░░░░░░░
    @staticmethod
    def rotate(nums: List[int], k: int) -> None:
        """
        三次翻转法: 通过局部翻转实现整体轮转
            1. 轮转定义 → 右移 k 位等价于将后 k 个元素移到前面
            2. 双指针翻转: 从两端向中间交换
            3. 边界处理: k %= n 防止 k > n 的情况
        """
        def reverse(_from: int, _to: int) -> None:
            while _from < _to:
                nums[_from], nums[_to] = nums[_to], nums[_from]
                _from += 1
                _to -= 1
        
        n = len(nums)
        k %= n
        reverse(0, n - 1)    # 整体翻转
        reverse(0, k - 1)    # 前 k 个翻转
        reverse(k, n - 1)    # 后 n-k 个翻转
