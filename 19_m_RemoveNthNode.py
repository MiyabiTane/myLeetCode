class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class  Solution(object):
    def removeNthFromEnd(self,head,n):
        #add 0 to head of the head
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        #put the first pointer on it's start
        for i in range(n+1):
            first=first.next
        #move two pointer
        while first!=None:
            first=first.next
            second=second.next #change the position of the pointer
        second.next=second.next.next #change dummy
        return dummy.next
