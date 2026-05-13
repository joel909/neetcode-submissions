class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dick_vals = []
        vals = [s,t]
        for val in vals:
            dick = {}
            for item in val:
                dick[item] = dick.get(item,0)+1
            dick_vals.append(dick)
        if dick_vals[0]==dick_vals[1]:
            return True
        return False
        