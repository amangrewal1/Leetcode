class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window = {}
        tmap = {}
        l = 0
        r = 0
        res = ""

        for char in t:
            if char not in tmap:
                tmap[char] = 0
            tmap[char] += 1
            window[char] = 0
        
        while r < len(s):
            if s[r] not in t:
                r += 1
                continue
            while l < len(s) and s[l] not in t:
                l += 1
            window[s[r]] += 1


            equal = True

            for key in tmap:
                if window[key] < tmap[key]:
                    equal = False
                    break
            
            if equal == True:
                sub = s[l:r+1]
                if res == "" or len(res) > len(sub):
                    res = sub
                window[s[l]] -= 1
                l += 1
                window[s[r]] -= 1
                r -= 1 

            r += 1
        
        return res






       
                    



            



        