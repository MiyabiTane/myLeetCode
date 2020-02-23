class ListNode(object):
    def __init__(self,x):
    self.val=x
    self.next=None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        #リスト→数字
        def GetNum(lst):
            num_list=[]
            while lst is not None:
                num_list.append(lst.val)
                lst=lst.next
            return num_list

        #２つの数字の和→リスト(左が１の位)
        def GetSum(num_l1,num_l2):
            sum1=0; sum2=0
            for i in range(len(num_l1)):
                sum1+=num_l1.pop()*(10**i)
            for i in range(len(num_l2)):
                sum2+=num_l2.pop()*(10**i)
            sum=sum1+sum2
            get_sum=[]
            while True:
                get_sum.append(sum%10)
                if sum<10:
                    break
                sum=sum//10
            return get_sum

        #リスト→リストノード
        def NumtoList(sum_list):
            answer=ListNode(0)
            dummy=answer
            for i in range(len(sum_list)):
                dummy.next=sum_list[i]
                dummy=dummy.next
            return answer.next

        num_l1=GetNum(l1)
        num_l2=GetNum(l2)
        sum_list=GetSum(num_l1,num_l2)
        answer=NumtoList(sum_list)
        return answer





