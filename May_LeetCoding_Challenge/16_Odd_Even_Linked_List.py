# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        count = 0
        odd = head
        even = head.next
        p1 = odd
        p2 = even
        while p1.next and p2.next:
            count += 1
            print("odd", odd)
            print("even", even)
            if count % 2 == 1:
                p1.next = p1.next.next
                p1 = p1.next
            else:
                p2.next = p2.next.next
                p2 = p2.next
        p1.next = p2
        return odd





