class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for n in tokens:
            if n in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if n == "+":
                    stack.append(num1 + num2)
                elif n == '-':
                    stack.append(num1 - num2)
                elif n == '*':
                    stack.append(num1 * num2)
                elif n == '/':
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(n))
            #print(stack)
        return stack.pop()


            
        