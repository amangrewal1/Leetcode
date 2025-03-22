class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        if nums[l] < nums[r]:
            return nums[l]

        while l != r:
            middle = round((r+l)/2)
            if (nums[r] - nums[middle]) < (nums[middle] - nums[l]):
                l = middle
            else:
                r = middle
            if r - l == 1:
                return min(nums[l], nums[r])
        
        return nums[l]
         
         
         
         
  
