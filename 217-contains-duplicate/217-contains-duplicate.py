class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)):
            try:
                if nums[i]==nums[i+1]:
                    return True
            except:
                return False
            
        return False