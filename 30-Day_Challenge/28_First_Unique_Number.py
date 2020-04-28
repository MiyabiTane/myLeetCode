class FirstUnique:
    def __init__(self, nums):
        self.queue = nums
        self.unique = []
        self.dupli = []
        for num in nums:
            if num in self.unique:
                self.unique.pop(self.unique.index(num))
                if not num in self.dupli:
                    self.dupli.append(num)
            elif not num in self.dupli:
                self.unique.append(num)

    def showFirstUnique(self):
        if self.unique:
            print(self.unique[0])
            return self.unique[0]
        print(-1)
        return -1

    def add(self, value):
        #print("add",value)
        if value in self.unique:
            self.unique.pop(self.unique.index(value))
            if not value in self.dupli:
                self.dupli.append(value)
        elif not value in self.dupli:
            self.unique.append(value)
        #print("uni", self.unique)
        #print("dup", self.dupli)


qu = FirstUnique([7,7,7,7,7])
qu.showFirstUnique()
qu.add(7)
qu.add(3)
qu.add(3)
qu.add(7)
qu.add(17)
qu.showFirstUnique()



