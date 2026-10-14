class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            intial_index = 0
            final_index = len(row)
            mid_index = -100
            while mid_index != int((final_index+intial_index)/2):
                mid_index = int((final_index+intial_index)/2)
                if row[mid_index]>target:
                    final_index = mid_index
                elif row[mid_index]<target :
                    intial_index = mid_index
                else:
                    return True
            # print("Bro dint dint find elemnt in row")
        return False
        
        