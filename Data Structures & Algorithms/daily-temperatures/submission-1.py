class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        index_stack = []
        numbers_stack = []
        peek_item = 100000
        for index,temp in enumerate(temperatures):
            if peek_item > temp:
                numbers_stack.append(temp)
                index_stack.append(index)

            else:
                # print("ghere")
                while peek_item<temp:
                    numbers_stack.pop()
                    removed_index = index_stack.pop()
                    delta_index = index-removed_index
                    result[removed_index] = delta_index
                    # print(result)
                    if len(numbers_stack) ==0:
                        break
                    peek_item = numbers_stack[-1]
                numbers_stack.append(temp)
                index_stack.append(index)

            peek_item = numbers_stack[-1]
        return result
        