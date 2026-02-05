class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxHeight = 0
        res = 0

        while l <= r:
            if height[l] == height[r]:
                maxHeight = max(maxHeight, height[l])
                if maxHeight - height[l] > 0:
                    res += maxHeight - height[l]
                    if l != r:
                        res += maxHeight - height[l]
                l += 1
                r -= 1

            elif height[l] < height[r]:
                maxHeight = max(maxHeight, height[l])
                if maxHeight - height[l] > 0:
                    res += maxHeight - height[l]
                l += 1
            else:
                maxHeight = max(maxHeight, height[r])
                if maxHeight - height[r] > 0:
                    res += maxHeight - height[r]
                r -= 1
        
        return res





            


        

        