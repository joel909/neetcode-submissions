class Solution:
    def trap(self, height: List[int]) -> int:
        def LTR_max_finder(array):
            max_value = 0
            max_value_cache = []
            for index in range(0,len(array)):
                if array[index] > max_value:
                    max_value = array[index]
                max_value_cache.append(max_value)
            return max_value_cache
        def RTL_max_finder(array):
            max_value = 0
            max_value_cache = []
            for index in range(len(array)-1,-1,-1):
                if array[index] > max_value:
                    max_value = array[index]
                max_value_cache.append(max_value)
            return max_value_cache[::-1]
        left_cache = LTR_max_finder(height)
        right_cache = RTL_max_finder(height)
        total_area = 0
        for index,item in enumerate(height):
             area = min(left_cache[index],right_cache[index]) - item
             if area > 0:
                 total_area += area
        return total_area
        