class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        three_sum_hash_set= set()
        for index,number in enumerate(nums):
            right_index = len(nums)-1
            left_index = 0
            required_number = 0 - number
            # print("c for number : ",number," with index : ",index)
            if number == nums[index-1] and index != 0:
                continue
            while left_index<right_index:
                if nums[left_index]+nums[right_index]==required_number and left_index != index and right_index != index :
                    # print("currenrlty checking numbers : ",nums[left_index]," and ",nums[right_index])
                    # print("a match is with index values is ","index : ", index," left index : ",left_index,"right_index : ",right_index)
                    # print("vlaues are : ",number," ",nums[left_index]," ",nums[right_index])
                    if left_index > index and right_index > index:
                        three_sum_hash_set.add(tuple(([number,nums[left_index],nums[right_index]])))
                    else:
                        # print("dint add cuz not compactabe;")
                        pass
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