class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        countA=0
        countB=0
        curA=headA
        curB=headB
        while curA:
            countA+=1
            cueA=curA.next
        while curB:
            countB+=1
            curB=curB.next
        while countA>countB:
            headA=headA.next
            countA-=1
        while countB>countA:
            headB=headB.next
            countB-=1
        while curA and curB:
            if curA==curB:
                return curA
            else:
                curA=curA.next
                curB=curB.next
        return None
