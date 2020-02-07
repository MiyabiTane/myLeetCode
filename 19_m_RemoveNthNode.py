class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class  Solution(object):
    def removeNthFromEnd(self,head,n):
        #get the length
        length=0
        copylist=head
        while copylist!=None:
            length+=1
            copylist=copylist.next
        #remove
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        count=0
        while first:
            if count==length-n:
                first.next=first.next.next
            else:
                first=first.next
        #print(head)
            count+=1
        return dummy.next
"""
list=ListNode([1,2,3,4,5])
solu=Solution()
head=solu.removeNthFromEnd(list,2)
#print(head)
"""
