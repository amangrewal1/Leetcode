class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
        
        for i in nums :
            if i not in d:
                d[i] = 1
            else :
                d[i] += 1
        results = []
        
        while (k != 0) :
            max_value = max(d, key=d.get)
            results.append(max_value)
            del d[max_value]
            k -= 1
        
        
        return results