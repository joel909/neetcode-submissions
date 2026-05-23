class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print("sorted nums: ", nums)
        final_list = []
        for i in range(0,len(nums)):
            # print("-----------NEXT NUMBER----------")
            a = nums[i]
            left_index = i+1
            right_index = (len(nums)-1)
            if a>0:
                break
            if i>=1 and nums[i] == nums[i-1]:
                continue
            # print("current num: ", nums[i],"left index: ", left_index, "right index: ", right_index)
            while left_index < right_index:
                left = nums[left_index]
                right = nums[right_index]
                # print("current num: ", a, "left: ", left, "right: ", right)
                if left+right+a < 0:
                    left_index += 1
                elif left+right+a > 0 :
                    right_index -= 1
                else:
                    final_list.append([a, left, right])
                    # print("found match")
                    right_index -= 1
                    left_index += 1
                    while nums[left_index] == nums[left_index-1] and left_index < right_index:
                        left_index += 1
        return final_list
        