class Solution:
    def findMin(self, nums: List[int]) -> int:
        #figure out how the nature of binary search to be performed
        reverse = False
        if nums[0]>nums[-1]:
            reverse = True
        else:
            return nums[0]
        left= 0
        right = len(nums)-1
        prev_number = nums[0]
        while right>=left:
            mid_point = (left+right)//2
            # print("mid point is : ",mid_point," left is : ",left,"right is : ",right)
            if reverse:
                # print("Prev number is ",prev_number," current num is : ",nums[mid_point])
                if prev_number<=nums[mid_point]:
                    prev_number = nums[mid_point]
                    left = mid_point+1
                elif nums[mid_point]<=nums[mid_point-1]:
                    # print("founder min number and that is : ",nums[mid_point])
                    # break
                    return nums[mid_point]
                else :
                    right = mid_point-1

        