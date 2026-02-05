class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0 
        r = 0
        res = 0
        track = {}

        for r in range(len(s)):
            if s[r] not in track:
                track[s[r]] = r
                res = max(res, r - l + 1)
            else:
                index = track[s[r]]
                while l <= index:
                    del track[s[l]]
                    l+=1
                track[s[r]] = r
        return res
        

