# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        curr = None
        i = 0
        dummy = ListNode()
        head = dummy
        while i+1 != len(lists):
            head.next = lists[i+1]
            dummy = head
            while lists[i+1]:
                if lists[i] and lists[i].val <= lists[i+1].val:
                    temp = lists[i].next
                    lists[i].next = dummy.next
                    dummy.next = lists[i]
                    dummy = lists[i]
                    lists[i+1] = lists[i].next
                    lists[i] = temp
                   
                else:
                    dummy = lists[i+1]
                    lists[i+1] = lists[i+1].next
            if lists[i]:
                dummy.next = lists[i]
            lists[i+1] = head.next
            i+=1
        return lists[-1]
