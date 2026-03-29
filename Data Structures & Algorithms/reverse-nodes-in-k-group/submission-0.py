# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        kk = head
        temp = head
        count = 0
        head2 = None
        prevtemp = None

        while temp:
            if not kk:
                break
            kk = kk.next
            count+= 1
            if count == k:
                pre = kk
                gh = temp
                while temp != kk:
                    next_node = temp.next  
                    temp.next = pre  
                    pre = temp  
                    temp = next_node  
                if not head2:
                    head2 = pre
                if prevtemp:
                    prevtemp.next = pre
                prevtemp = gh
                count = 0

        return head2