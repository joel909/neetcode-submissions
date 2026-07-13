class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dick = {}
        for item in s:
            if s_dick.get(item) is None:
                s_dick[item] = 1
            else :
                s_dick[item] = s_dick[item]+1
        t_dick = {}
        for item in t:
            if t_dick.get(item) is None:
                t_dick[item] = 1
            else :
                t_dick[item] = t_dick[item]+1
        if s_dick == t_dick:
            return True
        return False
        