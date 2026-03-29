# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        res = []
        i = 1
        lhead = None
        curr = head
        prev = ListNode()
        prev.next = head
        head = prev
        tail = None
        while i != right:
            temp = curr.next
            if i >= left:
                if not lhead:
                    tail = curr
                    lhead = prev
                curr.next = prev
            prev = curr
            curr = temp
            i+=1
        tail.next = curr.next
        curr.next = prev
        lhead.next = curr
        return head.next