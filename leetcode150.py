class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if stack and i in "+-*/":
                second = stack.pop()
                first = stack.pop()
                res = 0
                if i == "+":
                    res = str(int(first) + int(second))
                elif i == "-":
                    res = str(int(first) - int(second))
                elif i == "*":
                    res = str(int(first) * int(second))
                elif i == "/":
                    res = int(int(first) / int(second))
                stack.append(str(res))
            else:
                stack.append(i)
        
        return stack[0]