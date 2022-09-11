class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        l = 0 
        r = 0
        res = 0
        
        while l <= r and r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else :
                count[s[r]] += 1
            
            if (r-l +1) - max(count.values())  <= k :
                res = max(res, r-l+1)
                r += 1
            else :
                res = max(res, r-l)
                count[s[l]] -= 1
                count[s[r]] -= 1
                l += 1
            
        return res