class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        rl=list(s)
        tl=list(t)
        if len(rl) != len(tl):
            return False
        for i in rl:
            for k in range(0,len(tl)):
                if i == tl[k]:
                    del tl[k]
                    break
        if tl==[] :
            return True
        return False


                

        