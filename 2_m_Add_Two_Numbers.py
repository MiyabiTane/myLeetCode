class ListNode(object):
    def __init__(self,x):
    self.val=x
    self.next=None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
       answer=dummy=ListNode(0)
        carry=0   #繰り上がりの記憶
        while l1 or l2 or carry==1:
            num1=l1.val if l1 else 0
            num2=l2.val if l2 else 0
            #print(num1,num2)
            sum=num1+num2+carry
            if sum<10:
                carry=0
            else:
                carry=1 
            dummy.next=ListNode(sum%10) 
            #print(answer)
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            #print(l1)
            #print(l2)
            dummy=dummy.next
        return answer.next