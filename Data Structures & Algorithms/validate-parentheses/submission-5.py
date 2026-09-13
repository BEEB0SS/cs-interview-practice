class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == '(' or letter == '[' or letter == '{':
                stack.append(letter)
            elif letter == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif letter == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif letter == "}" :
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False