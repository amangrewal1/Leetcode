class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        deflection = -1

        if r == 0:
            if nums[r] == target:
                return r
            else:
                return -1
        if r == 1:
            if nums[r] == target:
                return r
            elif nums[l] == target:
                return l
            else:    
                return -1

        while l != r:
            m = (r + l) // 2
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        deflection = l
        l, r = 0, len(nums) - 1
        if target == nums[deflection]:
            return deflection
        elif target <= nums[r] and target >= nums[deflection]:
            l = deflection
        else:
            r = deflection

        while l != r:
            m = (r + l) // 2
            if target <= nums[m]: 
                r = m
            else:
                l = m + 1
        
        if nums[l] == target:
            return l
        else:
            return -1


                
        