class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        for i in set(nums):
            count = 0
            for k in range(0,len(set(nums))):
                if (i+k in set(nums)):
                    count +=1
                else:
                    break

            if (count>max_len):
                max_len = count
                    
        return max_len



        