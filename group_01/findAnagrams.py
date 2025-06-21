class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        cnt = Counter(p)
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while left <= right and cnt[c] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        return ans
