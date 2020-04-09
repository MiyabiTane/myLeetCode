class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = []
        self.head = -1
        self.tail = -1

    def enQueue(self, value: int) -> bool:
        if len(self.queue) != self.size:
            self.queue.append(value)
            self.tail += 1
            if self.head == -1:
                self.head = 0
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop(0)
        self.tail -= 1
        return True

    def Front(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[self.head]
    
    def Rear(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.queue[self.tail]
    
    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False
    
    def isFull(self) -> bool:
        if len(self.queue) == self.size:
            return True
        return False


circularQueue = MyCircularQueue(3)
print(circularQueue.enQueue(1))
print(circularQueue.enQueue(2))
print(circularQueue.enQueue(3))
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
print(circularQueue.isFull())
print(circularQueue.deQueue())
print(circularQueue.enQueue(4))
print(circularQueue.Rear())
