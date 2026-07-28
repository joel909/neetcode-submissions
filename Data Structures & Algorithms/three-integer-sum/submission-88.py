class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        three_sum_hash_set= list()
        for index,number in enumerate(nums):
            right_index = len(nums)-1
            left_index = index
            required_number = 0 - number
            # print("c for number : ",number," with index : ",index)
            if number == nums[index-1] and index != 0:
                continue
            selected_num = 0
            while left_index<right_index:
                if nums[left_index]+nums[right_index]==required_number and left_index != index and right_index != index :
                    # print("currenrlty checking numbers : ",nums[left_index]," and ",nums[right_index])
                    # print("a match is with index values is ","index : ", index," left index : ",left_index,"right_index : ",right_index)
                    # print("vlaues are : ",number," ",nums[left_index]," ",nums[right_index])
                    if nums[left_index-1] == nums[left_index] and left_index-1>=0 and selected_num != 0 :
                        left_index += 1
                        continue
                    elif right_index+1<len(nums) and selected_num != 0  :
                        if nums[right_index+1] == nums[right_index]:
                            right_index -=1
                            continue
                    three_sum_hash_set.append((([number,nums[left_index],nums[right_index]])))
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
            # del nums[index]
            # print("___________________________")

        return list(three_sum_hash_set)