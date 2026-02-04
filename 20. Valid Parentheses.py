# keep adding to list and negate with pop when we find a closing bracket

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        maps = {"}" :"{" , "]":"[" , ")":"("}
        for i in s:
            if i in maps:
                if brackets and brackets[-1] == maps[i]:
                    brackets.pop()
                else :
                    return False
            else:
                brackets.append(i)
        return bool( not brackets)
    

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        maps = {"}":"{", "]":"[", ")":"("}

        for a_b in s:
            if a_b in maps:
                if brackets and brackets[-1] == maps[a_b]:
                    brackets.pop()
                else:
                    return False
            else:
                brackets.append(a_b)
        return not brackets