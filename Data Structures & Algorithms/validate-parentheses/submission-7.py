class Solution:
    def isValid(self, s: str) -> bool:
        mystack = [s[0]]
        for index in range(1, len(s)):
            required_bracket = None
            if mystack == []:
                mystack.append(s[index])
                continue
            if mystack[-1] == "(":
                required_bracket = ")"
            elif mystack[-1] == "{":
                required_bracket = "}"
            elif mystack[-1] == "[":
                required_bracket = "]"
            if s[index] == required_bracket:
                mystack.pop()
            else:
                mystack.append(s[index])
        return len(mystack) == 0