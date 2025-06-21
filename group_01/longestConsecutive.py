class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0

        for x in seen:
            if x - 1 in seen:
                continue
            y = x + 1
            while y in seen:
                y += 1
            ans = max(ans, y - x)

        return ans
