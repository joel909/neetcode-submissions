class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t_len = len(nums)
        for i in range(0,t_len):
            for k in range(i+1,t_len):
                if nums[i]+nums[k] == target:
                    return [i,k]
        