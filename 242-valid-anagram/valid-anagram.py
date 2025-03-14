class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for letter in s:
            if letter not in d1:
                d1[letter] = 0
            d1[letter] += 1
        
        for letter in t:
            if letter not in d2:
                d2[letter] = 0
            d2[letter] += 1

        if d1 == d2:
            return True
        else :
            return False