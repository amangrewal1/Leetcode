class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        high = 0
        l = 0
        r = len(height) - 1

        while l < r :
            high = max(high, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]: 
                r -= 1
            else:
                l += 1
                r -= 1
        
        return high





        return high

