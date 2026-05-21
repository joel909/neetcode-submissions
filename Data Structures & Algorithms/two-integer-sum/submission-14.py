class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for index,item in enumerate(nums):
            required_num = target - item
            needs[required_num] = index
        for index, k in enumerate(nums):
            if k in needs and needs[k] != index:
                return [index,needs[k]]
        return []
        