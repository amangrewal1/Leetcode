class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d1 = defaultdict(int)
        l = 0
        res = 0


        for i in range(len(s)):
            d1[s[i]] += 1
            diff = sum(d1.values()) - max(d1.values())
            if (diff <= k):
                res = max(res, i - l + 1)
            else:
                d1[s[l]] -= 1
                l += 1
        
        return res