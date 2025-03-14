class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d1 = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in d1:
                return [d1[difference], i]
            else:
                d1[nums[i]] = i
        

            