# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 or l2
        head = cur = ListNode(0)
        while l1 and l2:
            #print(head)
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        #最後の数字
        cur.next = l1 or l2
        return head.next

#print(head)
ListNode{val: 0, next: None}
ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}
ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}}}
ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}}}
ListNode{val: 0, next: ListNode{val: 1, next: ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}}}}

#print(cur)
ListNode{val: 0, next: None}
ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 4, next: None}}}
ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 4, next: None}}}
ListNode{val: 2, next: ListNode{val: 4, next: None}}
ListNode{val: 3, next: ListNode{val: 4, next: None}}
