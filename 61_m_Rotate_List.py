class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #print(head)
        if head == None:
            return None
        if k == 0:
            return head

        def count_length(head):
            length = 0
            if head.next == None:
                return 1
            while head.next != None:
                length += 1
                head = head.next
            return length+1

        count = head
        length = count_length(count)
        while k >= length:
            k -= length
            if k == 0:
                return head
        #print("k is ",k)
        #print(length)
        remine = ListNode(0)
        rem_dummy = remine
        #頭のlen-k個をremineに。残りをheadに。
        for i in range(length-k):
            rem_dummy.next = ListNode(head.val)
            head = head.next
            rem_dummy = rem_dummy.next
        #print("remine is ",remine)
        #print("head is ",head)
        dummy = head
        #headのポインターを一番後ろに持ってくる
        while head.next != None:
            head = head.next
        head.next = remine.next
        return dummy

"""
solu=Solution()

init_list=ListNode(0)
init=init_list
for i in range(5):
    init_list.next=ListNode(i+1)
init=init.next
print(init)

ans=solu.rotateRight(init, 2)
print(ans)
"""

