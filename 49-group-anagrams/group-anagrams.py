class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d1 = {}

        for s in strs:
            tup = tuple(sorted(s))
            if tup not in d1:
                d1[tup] = []
            d1[tup].append(s)

    
        return list(d1.values())
            