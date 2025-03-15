class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d1 = {}
        d2 = {}
        res = []

        for i in nums:
            if i not in d1:
                d1[i] = 0
            d1[i] += 1
        
        for key, value in d1.items():
            if value not in d2:
                d2[value] = []
            d2[value].append(key)
        
        for i in reversed(sorted(d2.keys())):
            for i in d2[i]:
                res.append(i)
                k -= 1
            if k == 0:
                return res

