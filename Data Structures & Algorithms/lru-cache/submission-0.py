class LRUNode:
    def __init__(self, key = None, val = None):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Setup dummmy nodes
        self.head, self.tail = LRUNode(), LRUNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.mapping = {}

    # Remove node from LL
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # Add node to LL at the tail
    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1
        self.remove(self.mapping[key])
        self.add(self.mapping[key])
        return self.mapping[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            self.remove(self.mapping[key])
            self.mapping[key].val = value
            self.add(self.mapping[key])
            return

        if len(self.mapping) >= self.capacity:
            self.mapping.pop(self.head.next.key)
            self.remove(self.head.next)

        new_node = LRUNode(key=key, val=value)
        self.add(new_node)
        self.mapping[key] = new_node

        
