class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
        "+": lambda x, y: x + y, 
        "-": lambda x, y: x - y, 
        "*": lambda x, y: x * y, 
        "/": lambda x, y: x / y
        }
        def is_number(s):
            try:
                num = float(s)
                return True
            except ValueError:
                return False
        if len(tokens) == 1:
            temp = tokens.pop(0)
            if is_number(temp):
                return int(temp)
            else:
                return None
        while len(tokens) != 0:
            temp = tokens.pop(0)
            if is_number(temp):
                stack.append(temp)
                print(stack)
            elif stack:
                int1 = stack.pop()
                if stack:
                    int2 = stack.pop()
                    print(int1, temp, int2)
                    stack.append(operations[temp](int(int2), int(int1)))
                    print(stack)
        return int(stack.pop())