class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_positions = (sorted(position))
        time_taken=[]
        positions_speed_map = {}
        result_stack = []
        for index,car_position in enumerate(position):
            positions_speed_map[car_position] = speed[index]
        print(positions_speed_map)
        for index in range(0,len(sorted_positions)):
            time_taken.append((target-sorted_positions[index])/positions_speed_map[sorted_positions[index]])
        reversed(time_taken)
        # print(sorted_positions,time_taken)

        current_stack = [time_taken[-1]]
        positions_speed_map.pop(sorted_positions[-1])
        sorted_positions.pop()
        time_taken.pop()
        

        for index in range(-1,-len(sorted_positions)-1,-1):
            # print("comparing : ",time_taken[-1]," with : ",current_stack[0])
            if time_taken[-1]<=current_stack[0]:
                current_stack.append(time_taken[-1])
            else:
                result_stack.append(current_stack)
                current_stack =[time_taken[-1]]

            positions_speed_map.pop(sorted_positions[-1],0)
            sorted_positions.pop()
            time_taken.pop()
        result_stack.append(current_stack)
        # print(result_stack)
        return len(result_stack)