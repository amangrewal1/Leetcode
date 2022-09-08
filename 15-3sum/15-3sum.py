class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        lis = []
        nums.sort()

        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] :
                continue
        
            l = i + 1
            r = len(nums) - 1
            target = nums[i] * -1
            
            while l < r :
                if nums[l] + nums[r] > target :
                    r -= 1
                elif nums[l] + nums[r] < target :
                    l += 1
                else :
                    lis.append([nums[i], nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l < r:
                        l +=1
            
        return lis
            
        
     