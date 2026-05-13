class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        li = []
        muliply_cache = 1
        for i in range(0,len(nums)):
            val = 1
            for k in range(i+1,len(nums)):
                val = val*nums[k]
            val = val*muliply_cache
            muliply_cache = muliply_cache*nums[i]
            li.append(val)
        return li 
        
        