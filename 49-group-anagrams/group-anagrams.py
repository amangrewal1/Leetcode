class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d1 = {}

        for s in strs:
            tup = tuple(sorted(s))
            if tup not in d1:
                d1[tup] = []
            d1[tup].append(s)

        l1 = []
        for val in d1.values():
            l1.append(val)
        
        return l1
            