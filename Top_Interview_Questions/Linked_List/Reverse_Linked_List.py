# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def traceList(self, head: ListNode):
        vals = []
        while head:
           vals.append(head.val)
           head = head.next
        print(*vals)

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            keep = cur.next
            cur.next = prev
            prev = cur
            cur = keep
            #self.traceList(prev)
        return prev
