class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i in range(len(tokens)):
            # does order of operations mattter
            if(tokens[i] == "+"):
                a = stack.pop()
                b = stack.pop()
                c = a + b
                stack.append(c)
            elif(tokens[i] == "-"):
                a = stack.pop()
                b = stack.pop()
                c = b - a
                stack.append(c)
            elif(tokens[i] == "*"):
                a = stack.pop()
                b = stack.pop()
                c = a * b
                stack.append(c)
            elif(tokens[i] == "/"):
                a = stack.pop()
                b = stack.pop()
                # KEY: division always truncates toward zero
                c = int(b/a)
                stack.append(c)
            else:
                # add number to stack
                stack.append(int(tokens[i]))

        # remainder of stack = answer
        return stack.pop()
            
