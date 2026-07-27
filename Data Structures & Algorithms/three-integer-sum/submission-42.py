class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        three_sum_hash_set= set()
        for index,number in enumerate(nums):
            right_index = len(nums)-1
            left_index = 0
            required_number = 0 - number
            # print("c for number : ",number," with index : ",index)
            while left_index<right_index:
                # print("currenrlty checking numbers : ",nums[left_index]," and ",nums[right_index])
                if nums[left_index]+nums[right_index]==required_number and left_index != index and right_index != index:
                    # print("a match is with index values is ",index," ",left_index," ",right_index)
                    three_sum_hash_set.add(tuple(sorted([number,nums[left_index],nums[right_index]])))
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
            # print("___________________________")

        return list(three_sum_hash_set)
        