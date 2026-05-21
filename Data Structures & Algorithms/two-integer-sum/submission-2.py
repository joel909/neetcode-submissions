class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k = set(nums)
        indexes = set()
        i = 0
        for num in nums:
            if target-num in k:
                if target-num != num and len(k) == len(nums):
                    indexes.add(i)
                elif target-num == num and len(k) != len(nums):
                    indexes.add(i)
            i+=1
        return list(indexes)

        