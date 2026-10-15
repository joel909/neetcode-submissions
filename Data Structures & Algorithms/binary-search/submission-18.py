class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left  = 0
        right = len(nums)
        mid_index = (right+left)//2
        while left<=right and mid_index<=len(nums)-1:
            print("mid index is : ",mid_index)
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] > target:
                right = mid_index-1
            elif nums[mid_index] < target:
                left = mid_index+1
            # print(left,right,mid_index)
            mid_index = (right+left)//2
        return -1

        