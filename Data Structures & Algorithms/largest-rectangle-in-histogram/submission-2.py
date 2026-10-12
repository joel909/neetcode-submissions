class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0]+heights
        stack = [heights[-1]]
        stack_indexes = [len(heights)-1]
        indexes = [0]*len(heights)
        r2l_area = [0]*len(heights)
        l2r_area = [0]*len(heights)
        r2l_indexes = []
        l2r_indexes = []
        # print("heights for iteration 1 : ",heights)
        #movinng right to left first (top to bottom):
        for i in range(1,len(heights)):
            item_index = len(heights)-1-i
            if heights[item_index]>=stack[-1]:
                stack.append(heights[item_index])
                stack_indexes.append(item_index)
            else:
                #print("the element : ",heights[item_index]," is not greater than prev element in stack : ",stack[-1])
                # print("Stack : ",stack[-1])
                # print("height :",heights[item_index])
                while stack[-1]>heights[item_index]:
                    indexes[stack_indexes[-1]] = (stack_indexes[-1]-item_index-1)
                    r2l_area[stack_indexes[-1]] = ((stack_indexes[-1]-item_index-1))*stack[-1]
                    # print("stack index - : ",stack_indexes[-1]," new item index: ",item_index," the max for element :",stack[-1]," is ",item_index-stack_indexes[-1])
                    stack.pop()
                    stack_indexes.pop()
                    if len(stack) == 0:
                        break
                stack.append(heights[item_index])
                stack_indexes.append(item_index)
        r2l_indexes = indexes.copy()
        r2l_indexes = r2l_indexes[1::]
        # l2r_area.pop()


        heights.reverse()
        heights.pop()
        heights = [0]+heights
        # print("Heights for iteration 2 : ",heights)
        stack = [heights[-1]]
        stack_indexes = [len(heights)-1]
        indexes = [0]*len(heights)
        #movinng right to left first (top to bottom):
        for i in range(1,len(heights)):
            item_index = len(heights)-1-i
            if heights[item_index]>=stack[-1]:
                stack.append(heights[item_index])
                stack_indexes.append(item_index)
            else:
                #print("the element : ",heights[item_index]," is not greater than prev element in stack : ",stack[-1])
                # print("Stack : ",stack[-1])
                # print("height :",heights[item_index])
                while stack[-1]>heights[item_index]:
                    indexes[stack_indexes[-1]] = ((stack_indexes[-1]-item_index-1))
                    # print("adding : ",((stack_indexes[-1]-item_index-1)+1)*stack[-1],"to : ",r2l_area[stack_indexes[-1]])
                    l2r_area[stack_indexes[-1]] = ((stack_indexes[-1]-item_index-1)+1)*stack[-1]
                    # print("stack index - : ",stack_indexes[-1]," new item index: ",item_index," the max for element :",stack[-1]," is ",item_index-stack_indexes[-1])
                    stack.pop()
                    stack_indexes.pop()
                    if len(stack) == 0:
                        break
                stack.append(heights[item_index])
                stack_indexes.append(item_index)
        l2r_indexes = indexes.copy()
        l2r_indexes = l2r_indexes[-1:0:-1]
        # print("right to left : ",r2l_indexes)  
        # print("right to left : ",r2l_area[1::])           
        # print("left to right : ",l2r_indexes)
        l2r_area.reverse()
        result = [x + y for x, y in zip(r2l_area[1::], l2r_area[:-1:])]
        # print("left to right : ",l2r_area[:-1:])
        # print("max is : ",max(result))
        return max(result)
        