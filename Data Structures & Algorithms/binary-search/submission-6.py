class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_copy = nums.copy()
        intial_index = 0
        final_index = len(nums_copy)
        mid_index = -100
        while mid_index != int((final_index+intial_index)/2):
            mid_index = int((final_index+intial_index)/2)
            # print("mid index is : ",mid_index)
            # if final_index-intial_index==1 and mid_index != 0:
            #     # print("item was not found")
            #     return -1
            #     break 
            if nums_copy[mid_index]>target:
                final_index = mid_index
                # nums_copy = nums_copy[intial_index:final_index]
            elif nums_copy[mid_index]<target :
                intial_index = mid_index
            else:
                # print("Element was found on index : ",mid_index,"value is ",nums_copy[mid_index])
                # print("extreme indexes were : ",intial_index," final index was : ",final_index)
                return mid_index
        return -1

        