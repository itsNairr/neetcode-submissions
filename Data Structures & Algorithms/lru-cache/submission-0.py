class Node:
    def __init__(self, key, value):
        self.value = value
        self.next = None
        self.key = key
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashh = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hashh:
            node = self.hashh[key]
            self.move2back(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashh:
            node = self.hashh[key]
            node.value = value
            self.move2back(node)
        else:
            if len(self.hashh.keys()) == self.capacity:
                del self.hashh[self.head.key]
                if self.head == self.tail:
                    self.head = self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            nnode = Node(key, value)
            self.hashh[key] = nnode
            if self.head is None:
                self.head = self.tail = nnode
            else:
                self.tail.next, nnode.prev = nnode, self.tail
                self.tail = nnode 
            

    def move2back(self, node: Node) -> None:
        if self.tail == node:
            return
        if self.head == node:
            self.head = node.next
            node.next.prev = None
        else:
            node.next.prev, node.prev.next = node.prev, node.next
        
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
