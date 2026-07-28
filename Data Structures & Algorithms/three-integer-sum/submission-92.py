class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        three_sum_list= []
        for index,number in enumerate(nums):
            right_index = len(nums)-1
            left_index = index
            required_number = 0 - number
            if number == nums[index-1] and index != 0:
                continue
            selected_num = 0
            while left_index<right_index:
                if nums[left_index]+nums[right_index]==required_number and left_index != index and right_index != index :
                    if nums[left_index-1] == nums[left_index] and selected_num != 0 :
                        left_index += 1
                        continue
                    elif selected_num != 0 :
                        if nums[right_index+1] == nums[right_index]:
                            right_index -=1
                            continue
                    three_sum_list.append((([number,nums[left_index],nums[right_index]])))
                    selected_num +=1
                    right_index -= 1
                    left_index += 1
                    continue
                elif left_index == index:
                    left_index += 1
                    continue
                elif right_index == index:
                    right_index -= 1
                    continue
                elif nums[left_index]+nums[right_index]>required_number:
                    right_index -= 1
                    continue
                elif nums[left_index]+nums[right_index]<required_number:
                    left_index += 1
                    continue


        return three_sum_list