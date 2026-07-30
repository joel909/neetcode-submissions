class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len_heights = len(heights)
        left_index = 0
        right_index = len_heights - 1
        max_heights = 0
        while right_index>left_index:
            current_heights = min(heights[left_index],heights[right_index])*(right_index-left_index)
            print(right_index," ",left_index," current height",current_heights)
            if current_heights>max_heights:
                max_heights = current_heights
            else:
                if heights[left_index]>heights[right_index]:
                    right_index -= 1
                elif heights[left_index]<heights[right_index]:
                    left_index += 1
                else:
                    if left_index+1  < len_heights:
                        if heights[left_index+1]>heights[right_index]:
                            left_index += 1
                        else:
                            right_index -= 1
        return max_heights
        