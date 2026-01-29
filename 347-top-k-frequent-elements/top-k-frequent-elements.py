class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        count = {}
        for i in nums:
            count[i] = count.get(i,0) + 1
        heap = []

        for key in count:
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            



        
        
