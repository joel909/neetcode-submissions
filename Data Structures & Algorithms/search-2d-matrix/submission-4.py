class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #considering them as a single array
        length_per_row = len(matrix[0])
        total_rows = len(matrix)
        final_index = length_per_row*total_rows
        intial_index = 0
        mid_index = -100
        while mid_index != int((final_index+intial_index)/2):
            mid_index = int((final_index+intial_index)/2)
            #convert mid_index value in form of matrix
            row_no = mid_index//length_per_row
            index_within_row = mid_index-(row_no*length_per_row)
            # print("item is ",matrix[row_no][index_within_row])
            
            if matrix[row_no][index_within_row]>target:
                final_index = mid_index
                # print("A")
            elif matrix[row_no][index_within_row]<target :
                intial_index = mid_index
                # print("B")
            else:
                return True
        return False
        
        