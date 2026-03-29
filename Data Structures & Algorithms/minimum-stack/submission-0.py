class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        return self.stack.pop() if len(self.stack) != 0 else None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        temp = None
        for num in self.stack:
            if temp is None or num < temp:
                temp = num
        return temp
