class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)) :
            return False
        
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        
        if (s_sorted == t_sorted) :
            return True
        return False