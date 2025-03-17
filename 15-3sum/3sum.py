class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []

        
        for i in range(len(nums)):
            if nums[i] > 0 :
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1

            diff = nums[i] * -1

            while l < r:               
                target = nums[l] + nums[r]

                if diff == target :
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (l < r and nums[l] == nums[l-1]):
                        l+=1
                    r -= 1
                    while (l < r and nums[r] == nums[r+1]):
                        r -= 1
                elif diff > target:
                    l += 1
                else:
                    r -= 1
        

        return res

