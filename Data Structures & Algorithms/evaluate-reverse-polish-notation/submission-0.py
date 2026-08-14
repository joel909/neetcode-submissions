class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        current_stack = []
        for token in tokens:
            if token == "+":
                num2 = current_stack.pop()
                num1 = current_stack.pop()
                current_stack.append(num1+num2)
            elif token == "-":
                num2 = current_stack.pop()
                num1 = current_stack.pop()
                current_stack.append(num1-num2)
            elif token == "*":
                num2 = current_stack.pop()
                num1 = current_stack.pop()
                current_stack.append(num1*num2)
            elif token == "/":
                num2 = current_stack.pop()
                num1 = current_stack.pop()
                current_stack.append(int(num1/num2))
            else:
                current_stack.append(int(token))
        return current_stack.pop()
        