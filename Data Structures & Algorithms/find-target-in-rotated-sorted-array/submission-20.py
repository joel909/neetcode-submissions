class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target>=nums[0]:
            right = len(nums)-1
            left = 0
            while right>=left:
                mid_point = (right+left)//2
                print(nums[left:right+1])
                if nums[mid_point]<nums[0]:
                    right = mid_point-1
                    print("mkm")
                    continue

                if nums[mid_point]>target:
                    right = mid_point-1
                elif nums[mid_point]<target:
                    left = mid_point+1
                else:
                    return mid_point
        else:
            right = len(nums)-1 
            left = 0
            while right>=left:
                print(nums[left:right+1])
                mid_point = (right+left)//2
                print("Mid point it : ",nums[mid_point]," target is : ",target)
                if nums[mid_point]<target:
                    if nums[mid_point]<nums[0]:
                        left = mid_point+1
                    else:
                        right = mid_point-1
                elif nums[mid_point]>target:
                    if nums[mid_point]<nums[0]:
                        right = mid_point-1
                    else:
                        left = mid_point+1
                else:
                    return mid_point


        return -1
        