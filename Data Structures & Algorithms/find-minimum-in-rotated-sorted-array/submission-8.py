class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_index = -1
        if nums[0]<nums[-1]:
            min_index = len(nums)-1
            return nums[0]
        else:
            left = 0
            right = len(nums)-1
            while right>=left:
                mid_point = (left+right)//2
                if nums[mid_point-1]<nums[mid_point]:
                    if nums[0]>nums[mid_point]:
                        right = mid_point-1
                    else:
                        left = mid_point+1
                else:
                    # print("min number is : ",nums[mid_point+1])
                    return nums[mid_point]
                    
        