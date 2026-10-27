class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #do the case where if no element is in arrray is greater than target
        def get_min_index_larger_than_target(nums,target):
            if nums[-1]<target:
                return len(nums)
            elif nums[0]>target:
                return 0
            left = 0
            right = len(nums)-1
            while right>=left:
                # print("hi")
                mid_point = (right+left)//2
                if nums[mid_point]<target:
                    left = mid_point+1
                    if nums[left]>target:
                        return left
                elif nums[mid_point]>target:
                    right = mid_point-1
                    if nums[right]<target:
                        return mid_point
                else:
                    return mid_point
            return -1
        def get_median(array):
            if len(array)%2 != 0:
                    median_index = len(array)//2
                    return array[median_index]
            else:
                median_index1 = ((len(array)-1)//2)
                median_index2 = (len(array)//2)
                print("median index 1 : ",median_index1)
                print("Median index 2 : ",median_index2)
                return (array[median_index1]+array[median_index2])/2
            
        if nums1 == []:
            return get_median(nums2)
        elif nums2 == []:
            return get_median(nums1)
        else:
            for num in nums2:
                index_at_insert = get_min_index_larger_than_target(nums1,num)
                print("Adding : ",num," at index : ",index_at_insert)
                nums1.insert(index_at_insert,num)
            return get_median(nums1)