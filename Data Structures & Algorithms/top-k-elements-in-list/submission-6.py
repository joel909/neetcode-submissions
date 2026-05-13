class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kl = {}
        for num in nums:
            kl[num] = kl.get(num,0)+1
        l = []
        print(kl)
        for i in range(0,k):
            s = [0,0]
            for key in kl:
                if kl[key]>s[1]:
                    s[1] = kl[key]
                    s[0] = key
            del kl[s[0]]
            # print(kl)
            l.append(s[0])
        return l
                
                
        