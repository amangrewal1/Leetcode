class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ","")
        
        p1 = 0
        p2 = len(s) - 1

        if s == "":
            return True
    

        while (p1 <= p2):
            while (s[p1].isalnum() != True and p1 < p2):
                p1 += 1
            while (s[p2].isalnum() != True and p1 < p2):
                p2 -= 1
            if s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1
            else: 
                return False
        
        return True
