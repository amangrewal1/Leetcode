class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        
        for i, n in enumerate(nums) :
            
            desiredNum = target - nums[i]
            if desiredNum in hashmap :
                return [hashmap[desiredNum], i]
            hashmap[n] = i