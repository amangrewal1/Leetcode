class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        mySet = set()
        l = 0
        maxi = 0 
        
        for i in range(len(s)) :
            while s[i] in mySet:
                mySet.remove(s[l])
                l += 1
            mySet.add(s[i])
            maxi = max(maxi, len(mySet))
        return maxi
            