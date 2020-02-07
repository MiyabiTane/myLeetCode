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
        if length==1 or length==0:
            return None
        cur=head
        count=0
        while cur:
            if count==length-n-1:
                cur.next=cur.next.next
            else:
                cur=cur.next
        #print(head)
            count+=1
        return head
"""
list=ListNode([1,2,3,4,5])
solu=Solution()
head=solu.removeNthFromEnd(list,2)
#print(head)
"""
