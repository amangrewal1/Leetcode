class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d1 = set()

        for i in nums :
            if i in d1:
                return True
            else :
                d1.add(i)
        
        return False