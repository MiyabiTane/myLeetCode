# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


def BinarySearch(row):
    m = len(row)
    left = 0
    right = m - 1
    mid = (left + right) // 2
    #print(mid)
    while left < right:
        mid_num = row[mid]
        if mid != 0:
            mid_minus_1 = row[mid-1]
            if mid_num == 1 and mid_minus_1 == 0:
                return mid
        if mid != m-1:
            mid_plus_1 = row[mid+1]
            if mid_num == 0 and mid_plus_1 == 1:
                return mid+1
        if mid_num == 0:
            left = mid + 1
        if mid_num == 1:
            right = mid - 1
    return -1

ans = BinarySearch([0,1])
print(ans)

"""
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        n = binaryMatrix.dimensions(binaryMatrix)[0]
        #最も左にある1のインデックスを返す
        def BinarySearch(row_num, BinaryMatrix):
            m = binaryMatrix.dimensions(binaryMatrix)[1]
            left = 0; right = m - 1
            mid = (left + right) // 2
            while left <= right:
                mid_num = binaryMatrix.get(row_num, mid)
                if mid_num == 1 and mid == 0:
                    return 0
                mid_minus_1 = binaryMatrix.get(row_num, mid-1)
                if mid_num == 1 and mid_minus_1 == 0:
                    return mid
                mid_plus_1 = binaryMatrix.get(row_num, mid+1)
                if mid_num == 0 and mid_plus_1 == 1:
                    return mid+1
                elif mid_num == 0:
                    left = mid + 1
                elif mid_num == 1:
                    right = mid - 1
            return -1

        ans = 1000000000
        for i in range(n):
            keep = BinarySearch(i, binaryMatrix)
            if keep < ans:
                ans = keep
        return ans
"""           
        

                

