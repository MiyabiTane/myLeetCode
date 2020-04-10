class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack)>0:
            self.stack.pop(-1)

    def top(self) -> int:
        if len(self.stack)>0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack)>0:
            return min(self.stack)


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())


        
