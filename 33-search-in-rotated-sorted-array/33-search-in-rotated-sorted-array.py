class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        maxi = nums.index(max(nums))
        
        if (nums[0] <= target and target <= nums[maxi]) :
            l = 0
            r = maxi
            while l <= r :
                mid = (l+r) // 2
                if target < nums[mid] :
                    r = mid - 1
                elif target > nums[mid] :
                    l = mid + 1
                elif target == nums[mid] :
                    return mid
                else :
                    return -1
        elif maxi < (len(nums) - 1) :
            l = maxi + 1
            r = len(nums) - 1
            while l <= r :
                mid = (l+r) // 2
                if target < nums[mid] :
                    r = mid - 1
                elif target > nums[mid] :
                    l = mid + 1
                elif target == nums[mid] :
                    return mid
                else :
                    return -1  
        return -1