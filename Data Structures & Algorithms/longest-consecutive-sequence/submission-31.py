class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        # a = set(nums)
        for i in nums:
            count = 0
            for k in range(0,len(nums)):
                if (i+k in nums):
                    count +=1
                else:
                    break
            if (count>max_len):
                max_len = count
                    
        return max_len



        