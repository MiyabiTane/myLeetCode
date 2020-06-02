import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.

class CacheEntry:

    def __init__(self, url, contents):
        self.url = url
        self.contents = contents
        self.next = None
        self.prev = None 


class Cache:
    # Initializes the cache.
    # |n|: The size of the cache.
    def __init__(self, n):
        """
        entryDict = {url : CacheEntry}
        head oldest cacheEntry
        tail latest cacheEntry
        """
        self.n = n
        self.entryDict = {}
        self.head = None
        self.tail = None
    
    # Access a page and update the cache so that it stores the most
    # recently accessed N pages. This needs to be done with mostly O(1).
    # |url|: The accessed URL
    # |contents|: The contents of the URL
    def access_page(self, url, contents):
        #urlが既に辞書に存在する場合
        if url in self.entryDict:
            urlEntry = self.entryDict[url]
            #最新のurlだった場合、更新しなくて良い
            if not urlEntry == self.tail:
                if urlEntry == self.head:
                    self.head = urlEntry.next
                else:
                    urlEntry.prev.next = urlEntry.next

                urlEntry.next.prev = urlEntry.prev
                #urlを最後尾に持ってくる
                urlEntry.next = None
                self.tail.next = urlEntry
                urlEntry.prev = self.tail
                self.tail = urlEntry

        #urlが辞書になかった時
        else:
            newEntry = CacheEntry(url, contents)
            
            if self.tail:
                self.tail.next = newEntry
                newEntry.prev = self.tail
            self.tail = newEntry

            if not self.head:
                self.head = newEntry
            
            self.entryDict[url] = newEntry
            #cacheが溢れてしまう場合
            #ALEXNOTE: 辞書のlen()でサイズの管理して、よかったね。
            if len(self.entryDict) > self.n:
                del self.entryDict[self.head.url]
                self.get_pages()
                ＃ALEXNOTE：　上記のget_pagesはデバッグ用でしたか。
                self.head = self.head.next
                self.head.prev = None
                

    # Return the URLs stored in the cache. The URLs are ordered
    # in the order in which the URLs are mostly recently accessed.
    def get_pages(self):
        urls = []
        node = self.tail
        while node:
            urls.append(node.url)
            node = node.prev
        #print(urls)
        return urls

# Does your code pass all test cases? :)
def cache_test():
    # Set the size of the cache to 4.
    cache = Cache(4)
    # Initially, no page is cached.
    equal(cache.get_pages(), [])
    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # "a.com" is cached.
    equal(cache.get_pages(), ["a.com"])
    # Access "b.com".
    cache.access_page("b.com", "BBB")
    # The cache is updated to:
    #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
    equal(cache.get_pages(), ["b.com", "a.com"])
    # Access "c.com".
    cache.access_page("c.com", "CCC")
    # The cache is updated to:
    #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
    equal(cache.get_pages(), ["c.com", "b.com", "a.com"])
    # Access "d.com".
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
    # Access "d.com" again.
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    equal(cache.get_pages(), ["d.com", "c.com", "b.com", "a.com"])
    # Access "a.com" again.
    cache.access_page("a.com", "AAA")
    # The cache is updated to:
    #  (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
    equal(cache.get_pages(), ["a.com", "d.com", "c.com", "b.com"])
    cache.access_page("c.com", "CCC")
    equal(cache.get_pages(), ["c.com", "a.com", "d.com", "b.com"])
    cache.access_page("a.com", "AAA")
    equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
    cache.access_page("a.com", "AAA")
    equal(cache.get_pages(), ["a.com", "c.com", "d.com", "b.com"])
    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is full, so we need to remove the least recently accessed page "b.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
    equal(cache.get_pages(), ["e.com", "a.com", "c.com", "d.com"])
    # Access "f.com".
    cache.access_page("f.com", "FFF")
    # The cache is full, so we need to remove the least recently accessed page "c.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
    equal(cache.get_pages(), ["f.com", "e.com", "a.com", "c.com"])
    print("OK!")

# A helper function to check if the contents of the two lists is the same.


def equal(list1, list2):
    assert(list1 == list2)
    for i in range(len(list1)):
        assert(list1[i] == list2[i])


if __name__ == "__main__":
    cache_test()
