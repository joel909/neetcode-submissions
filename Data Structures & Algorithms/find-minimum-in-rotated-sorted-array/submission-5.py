class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<=nums[-1]:
            return nums[0]
        left= 0
        right = len(nums)-1
        prev_number = nums[0]
        while right>=left:
            mid_point = (left+right)//2
            if prev_number<=nums[mid_point]:
                prev_number = nums[mid_point]
                left = mid_point+1
            elif nums[mid_point]<=nums[mid_point-1]:
                return nums[mid_point]
            else :
                right = mid_point-1
        