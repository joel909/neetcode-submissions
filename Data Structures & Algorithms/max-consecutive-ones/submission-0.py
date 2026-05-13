class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_conc = 0
        temp_max = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                temp_max = temp_max +1
                if (len(nums)-1==i and temp_max>max_conc):
                    max_conc = temp_max
            else:
                if temp_max>max_conc:
                    max_conc = temp_max
                temp_max = 0
        return max_conc

        