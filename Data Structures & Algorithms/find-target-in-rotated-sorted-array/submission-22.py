class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##getting index of min value this will help us decide the nature of the binary search
        min_index = 0
        if nums[0]<nums[-1]:
            pass
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
                    min_index = mid_point
                    break
        # print("The min index was : ",min_index)
        right = len(nums)-1
        left = 0
        if target>nums[0]:
            right = min_index-1
            if right<0:
                right = len(nums)-1
            # print("new right is : ",right)
        elif nums[0]>target:
            left=min_index
            print("new left is : ",left)
        else:
            # print("The number is located at index : ",0)
            return 0
        while right>=left:
            mid_point = (right+left)//2
            # print("The mid point is  : ",mid_point)
            if nums[mid_point]>target:
                right = mid_point-1
            elif nums[mid_point]<target:
                left = mid_point+1
            else:
                return mid_point
                # print("The number is located at index : ",mid_point)
                break
        return -1
                    