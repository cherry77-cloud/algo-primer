class GeneralToolkit:
    # ░░░░░░░░░░░ LeetCode 169 —— 多数元素 ░░░░░░░░░░░
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        """
        Boyer-Moore 算法: 找出数组中出现次数超过 n/2 的元素
        核心思想: 不同元素相互抵消，最后剩下的就是多数元素
            1. 遇到相同元素：计数 +1（支持者）
            2. 遇到不同元素：计数 -1（反对者）
            3. 计数归零时：更换候选人
            4. 最终候选人必定是多数元素
        """
        candidate = None
        cnt = 0
        for num in nums:
            if cnt == 0:
                candidate = num
            cnt += (1 if num == candidate else -1)
            
        return candidate
