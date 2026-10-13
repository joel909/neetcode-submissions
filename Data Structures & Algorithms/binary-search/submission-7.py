class Solution:
    def search(self, nums: List[int], target: int) -> int:
        intial_index = 0
        final_index = len(nums)
        mid_index = -100
        while mid_index != int((final_index+intial_index)/2):
            mid_index = int((final_index+intial_index)/2)
            # print("mid index is : ",mid_index)
            # if final_index-intial_index==1 and mid_index != 0:
            #     # print("item was not found")
            #     return -1
            #     break 
            if nums[mid_index]>target:
                final_index = mid_index
                # nums = nums[intial_index:final_index]
            elif nums[mid_index]<target :
                intial_index = mid_index
            else:
                # print("Element was found on index : ",mid_index,"value is ",nums[mid_index])
                # print("extreme indexes were : ",intial_index," final index was : ",final_index)
                return mid_index
        return -1

        