class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        paran_map = {"(": ")",
                     "[": "]",
                     "{": "}"}
        for paran in s:
            if paran == "[" or paran == "(" or paran == "{":
                stack.append(paran)
            elif paran == "]" or paran == ")" or paran == "}":
                try: 
                    open_paran = stack.pop()
                    if paran_map[open_paran] != paran:
                        return False
                except:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
        