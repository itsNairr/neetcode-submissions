# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ll1, ll2 = [], []
        while l1:
            ll1.append(l1.val)
            l1 = l1.next
        
        while l2:
            ll2.append(l2.val)
            l2 = l2.next

        ll2.reverse()
        ll1.reverse()


        s1 = [str(i) for i in ll2]
        s2 = [str(i) for i in ll1]

        num1 = int("".join(s1))
        num2 = int("".join(s2))

        summ = num1 + num2

        suml = [int(i) for i in str(summ)]

        suml.reverse()

        head = ListNode(0)
        temp = head

        for num in suml:
            temp.next = ListNode(num)
            temp = temp.next

        return head.next
