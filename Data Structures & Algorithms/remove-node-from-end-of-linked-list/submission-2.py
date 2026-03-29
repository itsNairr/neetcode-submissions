# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return []
        master = head
        follower = head
        pre = None
        count = 0
        while master:
            master = master.next
            if count >= n:
                pre = follower
                follower = follower.next
            count += 1

        if follower == head:
            head = follower.next
        else:
            pre.next = follower.next
        follower.next = None

        return head
