class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def compute(t, a, b):
            if t == "+":
                return a + b
            elif t == "-":
                return a - b
            elif t == "*": 
                return a * b
            elif t == "/":
                return int(a / b)

        for t in tokens: 
            if t in set(["+", "-", "*", "/"]): 
                b = stack.pop()
                a = stack.pop()
                stack.append(compute(t, a, b))
            else: 
                stack.append(int(t))

        return stack.pop()
        
        