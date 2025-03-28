class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, tmap = {}, {}
        res = [-1,-1]
        l = 0

        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        have, need = 0, len(tmap)
        res, reslen = [-1, -1], float("infinity")
        
        for i in range(len(s)):
            c = s[i]
            window[c]  = 1 + window.get(c, 0)
            if c in t and window[c] == tmap[c]:
                have += 1
            while have == need:
                if reslen > (i - l +1):
                    res = [l,i]
                    reslen = i - l +1 
                window[s[l]] -= 1
                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1 
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""     