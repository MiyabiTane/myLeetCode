class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def getIntersectionNode(self,headA,headB):
        pA=headA
        pB=headB
        count=0
        while True:
            if count==2:
                break
            elif pA==pB:
                return pA
            elif pA or pB:
                if pA==None:
                    pA=headB
                    pB=pB.next
                    count+=1
                elif pB==None:
                    pA=pA.next
                    pB=headA
                else:
                    pA=pA.next
                    pB=pB.next
            else:
                pA=headB
                pB=headA
        return None
