class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    
       
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r]
                if target == curSum: 
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1 
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
                elif target < curSum:
                    r -= 1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1 
                else:
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        ans = [list(t) for t in res]
        return ans




