# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        lhead = None
        chead = head
        curr = head
        ftail = None
        tail = None
        i = 1
        while curr:
            if i == 1:
                check = curr
                for _ in range(k-1):
                    if check.next:
                        check = check.next
                    elif lhead:
                        lhead.next = temp
                        return ftail
                    else:
                        return head
            temp = curr.next
            curr.next = prev
            if i == k:
                tail = curr
                if not ftail:
                    ftail = curr
                else:
                   lhead.next = tail
                   chead.next = None
                lhead = chead
                chead = temp
                prev = temp
                i = 0
            else:
                prev = curr
            curr = temp
            i+=1
        return ftail