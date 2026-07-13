class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        final_list = []
        for item in nums:
            if item not in final_list:
                final_list.append(item)
            else :
                return True
        return False
        