class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        cnt_s = Counter(s)
        cnt_t = Counter(t)

        return cnt_s == cnt_t