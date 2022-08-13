class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)-1
        for i in range(0, len(nums)//2):
            if nums[i] == nums[i+1] or nums[n-i] == nums[n-i-1]:
                return True
        return False