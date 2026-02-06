class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_cnt = [0] * 26
        s2_cnt = [0] * 26


        for i in s1:
            s1_cnt[ord(i) - ord('a')] += 1

        l = 0

        for i in range(len(s2)):
            s2_cnt[ord(s2[i]) - ord('a')] += 1
            if i - l + 1 != len(s1):
                continue
            if s2_cnt == s1_cnt:
                return True
            else:
                s2_cnt[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False
        


       
        
            

                


        




