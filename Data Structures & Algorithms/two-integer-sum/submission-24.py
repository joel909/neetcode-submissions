class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        item_map = {}
        for index,item in enumerate(nums):
            item_map[item] = index
        for index,item in enumerate(nums):
            required = target-item
            if required in item_map and item_map[required] != index:
                return [index,item_map[required]] 
        