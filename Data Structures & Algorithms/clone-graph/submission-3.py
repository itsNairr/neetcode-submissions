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
            nnode = Node(node.val)
            nodelist[node.val] = nnode

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for n in curr.neighbors:
                    if n.val not in nodelist:
                        nn = Node(n.val)
                        nodelist[n.val] = nn
                        queue.append(n)
                    else:
                        nn = nodelist[n.val]
                    nodelist[curr.val].neighbors.append(nn)
                
        return nodelist[1]