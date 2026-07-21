class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_length = len(nums)
        right_sum = [1]
        final_product_list = []
        current_product = 1
        for i in range(-1,-total_length,-1):
            current_product *= nums[i]
            right_sum.append(current_product)
        left_sum = [1]
        current_product = 1
        for i in range(0,total_length-1):
            current_product *= nums[i]
            left_sum.append(current_product)
        for i in range(0,total_length):
            final_product_list.append(right_sum[total_length-i-1]*left_sum[i])
        return final_product_list