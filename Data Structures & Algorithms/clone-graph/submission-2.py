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

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.val not in nodelist:
                    ncurr = Node(curr.val)
                    nodelist[curr.val] = ncurr
                else:
                    ncurr = nodelist[curr.val]
                for n in curr.neighbors:
                    if n.val not in nodelist:
                        nn = Node(n.val)
                        nodelist[n.val] = nn
                        queue.append(n)
                    else:
                        nn = nodelist[n.val]
                    ncurr.neighbors.append(nn)
                
        return nodelist[1]