class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(ListNode):
    def __init__(self,x):
        ListNode.__init__(self,x)

    def mergeTwolists(self,l1,l2):
        head=cur=ListNode(0)
        while l1!=[] or l2!=[]:
            if l1==[] or l2.val<l1.val:
                cur.next=l2
                l2=l2.next
            elif l2==[] or l1.val<l2.val:
                cur.next=l1
                l1=l1.next
            cur=cur.next
        return head.next

#test=Solution()
