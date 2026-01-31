class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            target = nums[i] * -1
            while l<r:
                curSum = nums[l] + nums[r]
                if curSum > target:
                    r -= 1
                elif curSum < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l-1] == nums[l] and l < r:
                        l += 1
                    r -= 1
                    while nums[r+1] == nums[r] and l < r:
                        r -= 1
        return res




