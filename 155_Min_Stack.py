def MinStack(object):
    def __init__(self):
        self.minStack=[]

    def push(self,x):
        self.minStack.append(x)

    def pop(self):
        return self.minStack.pop()

    def top(self):
        if self.minStack:
            return minStack[-1]

    def getMin(self):
        if self.minStack:
            return min(self.minStack)
