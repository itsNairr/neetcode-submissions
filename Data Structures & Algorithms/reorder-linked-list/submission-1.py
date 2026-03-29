# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ftemp = head
        stemp = head

        while ftemp and ftemp.next:
            stemp = stemp.next
            ftemp = ftemp.next.next

        second = stemp.next
        stemp.next = None
        prev = None

        secondhead = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first, second = head, prev
        
        while second:
            temp = first.next
            first.next = second
            temp2 = second.next
            second.next = temp
            first = temp
            second = temp2

            
