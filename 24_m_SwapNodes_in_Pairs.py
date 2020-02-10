class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def swapPairs(self,head):
        dummy=ListNode(0)
        dummy.next=head
        p1=dummy
        while p1.next!=None and p1.next.next!=None:
            p2=p1.next
            p3=p2.next

            p1.next=p2.next
            p2.next=p3.next
            p3.next=p2
            p1=p2
        return dummy.next
