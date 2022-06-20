class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {"(":")","{":"}","[":"]"}
        stack = []
        for i in s:
            if i in "]})":
                if stack and i == hashMap[stack[-1]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return True if not len(stack) else False