"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        queue = deque()
        nodelist = {}
        if not node:
            return None
        else:
            queue.append(node)
            visited.add(node.val)
            nodelist[node.val] = Node(node.val)

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for n in curr.neighbors:
                    if n.val not in nodelist:
                        nodelist[n.val] = Node(n.val)
                        queue.append(n)
                    nodelist[curr.val].neighbors.append(nodelist[n.val])
                
        return nodelist[1]