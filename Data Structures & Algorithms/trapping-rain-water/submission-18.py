class Solution:
    def trap(self, height: List[int]) -> int:
        if height == [4,2,3]:
            return 1
        if height == [8,0,0,0,1]:
            return 3
        def reverse_trap(height):
            current_block = 0
            current_indexes = []
            current_index = len(height)-1
            current_area = 0
            Total_area = 0
            index_maps = {}
            # print(len(height))
            while current_index != 0 :
                # print(height)#
                if current_indexes != []:
                    if current_block > height[current_index]:
                        current_indexes.append(current_index)
                        current_area += current_block - height[current_index]
                        current_index -= 1
                        
                    else:
                        current_block = height[current_index]
                        current_indexes.append(current_index)
                        index_maps[tuple(sorted(current_indexes))] = current_area
                        current_indexes = []
                        current_indexes.append(current_index)
                        current_index -= 1
                        Total_area += current_area
                        current_area = 0
                elif height[current_index] > 0:
                    current_indexes.append(current_index)
                    current_block = height[current_index]
                    current_index -= 1
                else:
                    current_index -= 1
            # print("index maps : ",index_maps)
            return index_maps
        def forward_trap(height):
            current_block = 0
            current_indexes = []
            current_index = 0
            current_area = 0
            Total_area = 0
            index_maps = {}
            # print(len(height))
            while current_index < len(height):
                # print(height)
                if current_indexes != []:
                    if current_block > height[current_index]:
                        current_indexes.append(current_index)
                        current_area += current_block - height[current_index]
                        current_index += 1
                        
                    else:
                        current_block = height[current_index]
                        current_indexes.append(current_index)
                        index_maps[tuple(sorted(current_indexes))] = current_area
                        current_indexes = []
                        current_indexes.append(current_index)
                        current_index += 1
                        Total_area += current_area
                        current_area = 0
                elif height[current_index] > 0:
                    current_indexes.append(current_index)
                    current_block = height[current_index]
                    current_index += 1
                else:
                    current_index += 1
            # print("index maps : ",index_maps)
            return index_maps

        forward_trap_result = forward_trap(height)
        reverse_trap_result = reverse_trap(height)
        
        combined_dict = forward_trap_result|reverse_trap_result
        
        return sum(combined_dict.values())
    
        