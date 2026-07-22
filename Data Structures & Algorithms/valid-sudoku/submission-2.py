class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        location_map = {}
        for row in range(0,9):
            for column in range(0,9):
                location_map[(column,row)] = board[row][column]
        #check all rows 
        for row in range(0,9):
            current_row_numbers = [0]*10
            for column in range(0,9):
                if location_map[(column,row)] == ".":
                    continue
                else:
                    value = int(location_map[(column,row)])
                print("value : ",value)
                if current_row_numbers[value] != 0 :
                    print("did not work")
                    return False
                else:
                    current_row_numbers[value] = value
                    print(current_row_numbers," and the values are : ",current_row_numbers[value])
        for column in range(0,9):
                current_column_numbers = [0]*10
                for row in range(0,9):
                    if location_map[(column,row)] == ".":
                        continue
                    else:
                        value = int(location_map[(column,row)])
                    print("value : ",value)
                    if current_column_numbers[value] != 0 :
                        print("did not work")
                        return False
                    else:
                        current_column_numbers[value] = value
                        # print(current_column_numbers," and the values are : ",current_column_numbers[value])
        initial_row = 0
        initial_column = 0
        for index in range(0,9):
            print("IIIII : ",index)
            if index < 3 and index != 0:
                initial_row += 3
            elif index == 3:
                initial_row = 0
                initial_column += 3
            elif index > 3 and index < 6:
                initial_row += 3
            elif index == 6:
                initial_row = 0
                initial_column += 3
            elif index>6 and index < 9:
                initial_row += 3
            current_nine_square_numbers = [0]*10
            for col in range(initial_column,initial_column+3):
                    for row in range(initial_row,initial_row+3):
                        print(col,row)
                        if location_map[(col,row)] == ".":
                            print("continues","col : ",col,"row : ",row,"i : ",index)
                            continue
                        else:
                            value = int(location_map[(col,row)])
                        # print("value : ",value)
                        if current_nine_square_numbers[value] != 0 :
                            # print("did not work")
                            print("retuned false")
                            return False
                        else:
                            current_nine_square_numbers[value] = value
        return True