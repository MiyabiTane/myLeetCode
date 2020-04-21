# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        if not binaryMatrix:
            return -1
        m = binaryMatrix.dimensions()[0]
        n = binaryMatrix.dimensions()[1]
        pointer = [m-1, n-1]
        while True:
            num = binaryMatrix.get(pointer[0], pointer[1])
            if num == 0:
                if pointer[0] == 0:
                    if pointer[1] == n-1:
                        return -1
                    return pointer[1]+1
                pointer[0] -= 1
            else:
                if pointer[1] == 0:
                    return 0
                pointer[1] -= 1
        
        



