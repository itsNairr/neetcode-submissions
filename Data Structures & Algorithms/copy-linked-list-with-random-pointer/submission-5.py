"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        curr = dummy
        temp = head
        l = {}

        while temp:
            l[temp] = Node(temp.val, None, None)
            if temp.random:
                l[temp].random = temp.random
            temp = temp.next
        
        for node in l.values():
            curr.next = node
            if curr.next.random:
                curr.next.random = l[curr.next.random]
            curr = curr.next
        return dummy.next
            