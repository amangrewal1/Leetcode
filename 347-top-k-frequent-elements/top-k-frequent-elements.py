class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        cnt = Counter(nums)
        
        freq = cnt.most_common(k)
        res = []

        for i in freq:
            res.append(i[0])
        return res

        
        
