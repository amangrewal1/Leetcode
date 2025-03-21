class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window = {}
        tmap = {}
        res = ""
        l = 0

        for char in t:
            if char not in tmap:
                tmap[char] = 0
            tmap[char] += 1
            window[char] = 0
        have = 0
        need = len(t)
        
        for i in range(len(s)):
            if s[i] in t:
                window[s[i]] += 1
                if window[s[i]] <= tmap[s[i]]:
                    have += 1
            while have == need:
                sub = s[l:i+1]
                if res == "":
                    res = sub
                elif len(res) > len(sub):
                    res = sub 
                if s[l] in t:
                    window[s[l]] -= 1
                    if window[s[l]] < tmap[s[l]]:
                        have -= 1
                l += 1 

        return res     



            
    



       
                    



            



        