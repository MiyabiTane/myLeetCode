class FirstUnique:
    def __init__(self, nums):
        self.queue = []
        self.seen = {}
        for num in nums:
            if num in self.seen:
                self.seen[num] += 1
            else:
                self.seen[num] = 1
                self.queue.append(num)

    def showFirstUnique(self):
        if len(self.queue) == 0:
            print(-1)
            return -1
        while self.queue:
            num = self.queue[0]
            if self.seen[num] > 1:
                self.queue.pop(0)
            else:
                print(num)
                return num
        print(-1)
        return -1

    def add(self, value):
        if value in self.seen:
            self.seen[value] += 1
        else:
            self.seen[value] = 1
            self.queue.append(value)

qu = FirstUnique([7,7,7,7,7])
qu.showFirstUnique()
qu.add(7)
qu.add(3)
qu.add(3)
qu.add(7)
qu.add(17)
qu.showFirstUnique()



