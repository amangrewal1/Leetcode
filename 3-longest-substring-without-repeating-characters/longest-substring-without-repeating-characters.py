class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        leng = 1
        l = 0
        r = 1
        ss = set()


        if len(s) == 0:
            return 0
        
        ss.add(s[l])

        while r < len(s):
            print(ss)
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
            



                

            