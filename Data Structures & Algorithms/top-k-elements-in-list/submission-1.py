class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kl = {}
        for num in nums:
            kl[num] = kl.get(num,0)+1
        l = []
        print(kl)
        for i in range(0,k):
            val = 0
            num = 0
            for key in kl:
                if kl[key]>val:
                    val = kl[key]
                    num = key
            del kl[num]
            print(kl)
            l.append(num)
        return l
                
                
        