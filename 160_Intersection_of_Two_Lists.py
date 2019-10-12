class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        if headA is None or headB is None:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

"""
>>> while a!=10:
...     b = 1 if a%2==0 else 2
...     print(b)
...     a+=1
...
1
2
1
2
1
2
1
2
1
2
"""
