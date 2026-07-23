class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_map = {}
        starting_points =[]
        for num in nums:
            number_map[num] = 1
        for num in nums:
            if num-1 in number_map:
                pass
            elif num+1 in number_map:
                starting_points.append(num)
        max_count = 1
        if nums==[]:
            return 0
        current_count = 1
        for num in starting_points:
            current_count = 1
            for i in range(1,len(nums)+1):
                if num+i in number_map:
                    current_count+=1
                else:
                    break
            if current_count>=max_count:
                max_count = current_count
        return max_count

        


        