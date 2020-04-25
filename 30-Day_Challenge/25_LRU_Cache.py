class LRUCache:
    def __init__(self, capacity: int):
         self.cache = {}
         self.capacity = capacity
         self.seen = {} #key,number(大きいほど最新)

    def get(self, key: int) -> int:
        if key in self.cache:
            print(self.cache[key])
            self.seen[key] = max(self.seen.values()) + 1
            return self.cache[key]
        print(-1)
        return -1

    def put(self, key: int, value: int) -> None:
        if not key in self.cache:
            self.cache[key] = value
            if len(self.seen) == 0:
                self.seen[key] = 0
            else:
                self.seen[key] = max(self.seen.values()) + 1
        else: #ここは問題設定ミスな気がする
            self.cache[key] = value
            self.seen[key] = max(self.seen.values()) + 1

        if len(self.cache) > self.capacity:
            pop_value = min(self.seen.values())
            pop_key = [k for k, v in self.seen.items() if v == pop_value][0]
            self.cache.pop(pop_key)
            self.seen.pop(pop_key)
        print(self.cache, self.seen)

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
