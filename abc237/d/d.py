n = int(input())
s = input()
l = list(s)

class Node:
    def __init__(self, val):
        self.value = val
        self.right = None
        self.left= None

class BinarySearch:
    def __init__(self):
        self.root = Node(0)
    
    def right(self, val):
        node = Node(val)
        root = self.search(val)
        root.right = node

    def left(self, val):
        node = Node(val)
        root = self.search(val)
        root.left = node
    
    def search(self, value):
        def _search(node, value):
            if node.value == value:
                return node
            elif node.value > value:
                return _search(node.left, value)
            elif node.value < value:
                return _search(node.right, value)
        return _search(self.root, value)

    def in_order(self) -> None:
        def _in_order(node: Node) -> None:
            if node is not None:
                _in_order(node.left)
                print(node.value)
                _in_order(node.right)
        _in_order(self.root)

root_node = BinarySearch()

for i in range(0, len(l)):
    if l[i] == 'L':
        root_node.left(i+1)
    else:
        root_node.right(i+1)
print(root_node.in_order)
