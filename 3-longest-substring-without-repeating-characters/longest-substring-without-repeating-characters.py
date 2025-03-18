class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        leng = 0
        l = 0
        r = 0
        ss = set()

    
        while r < len(s):
            if s[r] in ss:
                while s[l] != s[r]:
                    ss.remove(s[l])
                    l += 1
                l += 1
                r += 1
            else:
                ss.add(s[r])
                r += 1
                leng = max(leng, len(ss))
        
        return leng
            



                

            