class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        hashset = {}
        
        for i, n in enumerate(numbers) :
            desiredNum = target - numbers[i]
            
            if desiredNum in hashset :
                return [hashset[desiredNum] + 1, i+1]
            hashset[n] = i