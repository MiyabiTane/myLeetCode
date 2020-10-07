# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_node = ListNode()
        head = new_node
        if not l1:
            return l2
        if not l2:
            return l1
        while True:
            if l1.val <= l2.val:
                new_node.val = l1.val
                l1 = l1.next
            else:
                new_node.val = l2.val
                l2 = l2.next
            if (not l1) or (not l2):
                if not l1:
                    new_node.next = l2
                else:
                    new_node.next = l1
                return head
            new_node.next = ListNode()
            new_node = new_node.next
        return None
