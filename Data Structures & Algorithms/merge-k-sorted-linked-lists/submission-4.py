# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []

        for l in lists:
            curr = l
            while curr:
                res.append(curr.val)
                curr = curr.next
        
        res.sort()

        dummy = ListNode(0)
        cur = dummy
        for num in res:
            temp = ListNode(num)
            cur.next = temp
            cur = cur.next
        return dummy.next
        