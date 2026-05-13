class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        dick_vals = []
        for val in strs:
            dick = {}
            for item in val:
                dick[item] = dick.get(item,0)+1
            k=0
            for i in range(0,len(dick_vals)):
                if dick==dick_vals[i][0]:
                    dick_vals[i].append(dick)
                    final[i].append(val)
                    k=1
            if(k==0):
                dick_vals.append([dick])
                final.append([val])

        return final
        