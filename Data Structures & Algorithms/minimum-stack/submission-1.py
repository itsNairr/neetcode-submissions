class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minn:
            self.minn.append(min(val, self.minn[-1]))
        else:
            self.minn.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minn.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
        
