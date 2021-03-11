class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # ノードの後ろ半分をひっくり返す
        rev = None
        while slow:
            nxt = slow.next
            slow.next = rev
            rev = slow
            slow = nxt
        # 前半とひっくり返した後半を比較
        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True




        
