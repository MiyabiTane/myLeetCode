class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def hasCycle(self,head):
        ListRemine=[]
        while head:
            if head in ListRemine:
                return True
            else:
                ListRemine.append(head)
                head=head.next
        return False
        
#head.valではなくheadごとみないと同じ数字が出現しただけでループとみなしてしまう
