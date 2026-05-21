class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for index,item in enumerate(nums):
            required_num = target - item
            print("index",index)
            needs[required_num] = index
        print("needs: ", needs)
        for index, k in enumerate(nums):
            print("index is ",index,"chekcing for ",k)
            if k in needs and needs[k] != index:
                print("found a match item was needed for item at index  ",needs[k])
                return [index,needs[k]]
        return []
        