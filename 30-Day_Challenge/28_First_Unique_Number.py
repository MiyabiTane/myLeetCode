import collections
class FirstUnique:

    def __init__(self, nums):
        self.queue = nums
        self.unique = collections.OrderedDict()
        for num in nums:
            if num in self.unique:
                self.unique.pop(num)
            else:
                self.unique[num] = 0
                
    def showFirstUnique(self):
        if self.unique:
            item = self.unique.popitem(last = False)[0] #先頭のkey取り出し
            self.unique[item] = 0
            self.unique.move_to_end(item, False) #itemを先頭へ移動
            print(item)
            print(self.unique)
            return item
        print(-1)
        return -1

    def add(self, value):
        if value in self.unique:
            self.unique.pop(value)
        else:
            self.unique[value] = 0
        print(self.unique)


qu = FirstUnique([7, 7, 7, 7, 7, 7])
qu.showFirstUnique()
qu.add(7)
qu.add(3)
qu.add(3)
qu.add(7)
qu.add(17)
qu.showFirstUnique()



