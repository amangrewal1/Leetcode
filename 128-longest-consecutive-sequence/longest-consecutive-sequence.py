class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        res = 1
        k = 1

        if len(nums) == 0:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] - 1:
                k += 1
                if k > res :
                    res = k
            elif nums[i] == nums[i+1]:
                continue
            else:
                k = 1
        
        return res




