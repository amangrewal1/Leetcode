class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window = {}
        tmap = {}
        res = ""
        l = 0

        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
            window[c] = 0
        have = 0
        need = len(t)
        reslen = 0
        
        for i in range(len(s)):
            if s[i] in t:
                window[s[i]] += 1
                if window[s[i]] <= tmap[s[i]]:
                    have += 1
            while have == need:
                sub = s[l:i+1]
                if reslen == 0:
                    res = sub
                    reslen = i - l +1
                elif reslen > (i - l +1):
                    res = sub
                    reslen = i - l +1 
                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1 

        return res     



            
    



       
                    



            



        