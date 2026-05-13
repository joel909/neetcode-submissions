class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        a = set(nums)
        for i in a:
            count = 0
            if (i-1 in a):
                pass
            else:
                for k in range(0,len(a)):
                    if (i+k in a):
                        count +=1
                    else:
                        break
                if (count>max_len):
                    max_len = count
                    
        return max_len



        