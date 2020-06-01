import sys

# Cache is a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library (e.g., collections.OrderedDict).
#       Implement the data structure yourself.
class Cache:
  # Initializes the cache.
  # |n|: The size of the cache.
  def __init__(self, n):
    """
    self.cache = {"url" : "contents"}
    self.lookup = {"url" : ["previous_url", "next_url"]}
    self.head = oldest url in cache
    self.tail = latest url in cache
    """
    self.cache = {}
    self.lookup = {}
    self.head = None
    self.tail = None
    self.n = n

  # Access a page and update the cache so that it stores the most
  # recently accessed N pages. This needs to be done with mostly O(1).
  # |url|: The accessed URL
  # |contents|: The contents of the URL
  def access_page(self, url, contents):
    
    if len(self.cache) == 0:
      self.head = url
      self.tail = url
      self.cache[url] = contents
      self.lookup[url] = [None, None]
      return

    elif url in self.cache:
      (pre, nxt) = self.lookup[url]
      if nxt == None:
        return
      if pre == None:
        self.head = nxt
      #update lookup 
      if not pre == None:
        self.lookup[pre][1] = nxt
      self.lookup[nxt][0] = pre
    
    elif len(self.cache) >= self.n:
      new_head = self.lookup[self.head][1]
      #update cache
      del self.cache[self.head]
      self.cache[url] = contents
      #update lookup
      del self.lookup[self.head]
      self.head = new_head
      self.lookup[self.head][0] = None

    #update cache
    self.cache[url] = contents
    #set url at tail
    self.lookup[self.tail][1] = url
    self.lookup[url] = [self.tail, None]
    self.tail = url
    

  # Return the page which is seen latest
  def get_latest_page(self):
    """
    if cache doesn't have any info, return []
    """
    if len(self.cache) == 0:
      return []
    return self.cache[self.tail]


# Does your code pass all test cases? :)
def cache_test():
  # Set the size of the cache to 4.
  cache = Cache(4)
  # Initially, no page is cached.
  equal(cache.get_latest_page(), [])
  # Access "a.com".
  cache.access_page("a.com", "AAA")
  # "a.com" is cached.
  equal(cache.get_latest_page(), "AAA")
  # Access "b.com".
  cache.access_page("b.com", "BBB")
  # The cache is updated to:
  #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "BBB")
  # Access "c.com".
  cache.access_page("c.com", "CCC")
  # The cache is updated to:
  #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "CCC")
  # Access "d.com".
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "DDD")
  # Access "d.com" again.
  cache.access_page("d.com", "DDD")
  # The cache is updated to:
  #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "DDD")
  # Access "a.com" again.
  cache.access_page("a.com", "AAA")
  # The cache is updated to:
  #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "AAA")
  cache.access_page("c.com", "CCC")
  equal(cache.get_latest_page(), "CCC")
  cache.access_page("a.com", "AAA")
  equal(cache.get_latest_page(), "AAA")
  cache.access_page("a.com", "AAA")
  equal(cache.get_latest_page(), "AAA")
  # Access "e.com".
  cache.access_page("e.com", "EEE")
  # The cache is full, so we need to remove the least recently accessed page "b.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "EEE")
  # Access "f.com".
  cache.access_page("f.com", "FFF")
  # The cache is full, so we need to remove the least recently accessed page "c.com".
  # The cache is updated to:
  #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
  equal(cache.get_latest_page(), "FFF")
  print("OK!")

# A helper function to check if the contents of the two lists is the same.
def equal(list1, list2):
  assert(list1 == list2)
  for i in range(len(list1)):
    assert(list1[i] == list2[i])

if __name__ == "__main__":
  cache_test()
