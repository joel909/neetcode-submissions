class Solution:
    def search(self, nums: List[int], target: int) -> int:
        intial_index = 0
        final_index = len(nums)
        mid_index = -100
        while mid_index != int((final_index+intial_index)/2):
            mid_index = int((final_index+intial_index)/2)
            if nums[mid_index]>target:
                final_index = mid_index
            elif nums[mid_index]<target :
                intial_index = mid_index
            else:
                return mid_index
        return -1

        