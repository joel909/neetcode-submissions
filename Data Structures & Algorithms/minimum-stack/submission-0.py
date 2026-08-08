class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest_digit_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.smallest_digit_stack == []:
            self.smallest_digit_stack.append(val)
        else:
            top_item = self.smallest_digit_stack[-1]
            if val<top_item:
                self.smallest_digit_stack.append(val)
            elif val==top_item:
                self.smallest_digit_stack.append(val)


    def pop(self) -> None:
        poped_item = self.stack.pop()
        if self.smallest_digit_stack[-1] == poped_item:
            self.smallest_digit_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest_digit_stack[-1]
        
