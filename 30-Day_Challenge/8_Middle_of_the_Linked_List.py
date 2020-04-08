class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def middleNode(head):
        dummy1 = head #毎回進む
        dummy2 = head #2回に1回進む
        count=1
        while dummy1.next!=None:
            dummy1 = dummy1.next
            if count==1:
                count=0
            elif count==0:
                dummy2 = dummy2.next
                count=1
        if count==0: #長さが偶数だった時
            dummy2 = dummy2.next 
        return dummy2





