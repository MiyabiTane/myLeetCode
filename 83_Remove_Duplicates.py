class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def deleteDuplicates(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=ans=ListNode(0)

        while head:
                forward=head.val
                ans.next=forward
                head=head.next
                if forward!=head.val:
                    ans=ans.next
                    ans.next=head.val
                ans=ans.next
        return cur.next
