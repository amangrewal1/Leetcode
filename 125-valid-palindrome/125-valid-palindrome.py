class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = []
        
        for i in s:
            if i.isalnum() :
                a.append(i)
        
        if a == a[::-1]:
            return True
        else :
            return False
            