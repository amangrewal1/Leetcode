class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d1 = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []

        for i in nums:
            if i not in d1:
                d1[i] = 0
            d1[i] += 1
        
        for key, value in d1.items():
            freq[value].append(key)
        
        for i in range(len(freq) -1, 0, -1):
            for j in freq[i]:
                res.append(j)
                k -= 1
            if k == 0:
                return res


