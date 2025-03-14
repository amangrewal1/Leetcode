class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}

        for letter in s:
            if letter not in d1:
                d1[letter] = 0
            d1[letter] += 1
        
        for letter in t:
            if letter not in d1:
                return False
            d1[letter] -= 1

        for val in d1.values():
            if val != 0:
                return False
        
        return True