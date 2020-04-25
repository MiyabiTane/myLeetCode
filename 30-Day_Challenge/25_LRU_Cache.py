import collections
class LRUCache:
    def __init__(self, capacity: int):
        #並び順つき辞書！
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            print(self.cache[key])
            value = self.cache.pop(key)
            self.cache[key] = value #順番更新
            return value
        print(-1)
        return -1

    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            self.cache[key] = value
        else: #ここは問題設定ミスな気がする
            self.cache.pop(key)
            self.cache[key] = value  

        if self.capacity > 0:
            self.capacity -= 1
        else: 
            #last = True -> LIFO, last = False -> FIFO
            self.cache.popitem(last = False)
            self.cache[key] = value
        print(self.cache)

cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
cache.get(2)
cache.put(1, 1)
#cache.get(2)
cache.put(4, 1)
cache.get(2)
#cache.get(3)
#cache.get(4)

#["LRUCache", "put", "put", "get", "put", "put", "get"]
#[[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]
