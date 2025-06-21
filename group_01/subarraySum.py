class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        pre_s = 0
        cnt = defaultdict(int)

        for x in nums:
            cnt[pre_s] += 1
            pre_s += x
            ans += cnt[pre_s - k]
        return ans
