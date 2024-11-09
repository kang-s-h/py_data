class TNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    from CircularQueue import CircularQueue
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:
        return 0
    elif n.isLeaf():
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    return max(hLeft, hRight) + 1