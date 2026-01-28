class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, val in enumerate(nums):
            if target - val in seen:
                return [idx, seen[target - val]]
            else:
                seen[val] = idx
        


        
