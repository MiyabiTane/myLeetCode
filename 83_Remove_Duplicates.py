class Solution(object):
    def deleteDuplicates(self,head):
        cur=head
        while cur:
            if cur.next and cur.next.val==cur.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
            #print(cur)
            #print(head)
        return head
