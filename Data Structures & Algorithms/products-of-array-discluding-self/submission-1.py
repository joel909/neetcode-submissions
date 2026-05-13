class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_cache = []
        muliply_cache = 1
        for i in range(0,len(nums)):
            l_cache.append(muliply_cache)
            muliply_cache = muliply_cache*nums[i]
        r_cache = []
        muliply_cache = 1
        for i in range(0,len(nums)):
            print("here")
            index = (len(nums)-1)-i
            r_cache.insert(0,muliply_cache*l_cache[index])
            muliply_cache = muliply_cache*nums[index]
        return (r_cache)
        
        