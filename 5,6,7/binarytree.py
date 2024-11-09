class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
def search_bst(n, key):
    if n is None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

def search_min_bst(n):
    while n is not None and n.left is not None:
        n = n.left
    return n

def search_max_bst(n):
    while n is not None and n.right is not None:
        n = n.right
    return n

def search_value_bst(n, value) :
    if n == None :
        return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None :
       return res
    return search_value_bst(n.right, value)

def insert_bst(root, node):
    if root is None:
        return node
    if node.key == root.key:
        return root  
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root

def delete_bst(root, key):
    if root is None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)
    else:
        if root.left is None:  
            return root.right
        elif root.right is None: 
            return root.left
        
        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    
    return root


class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst(self.root)

    def findMin(self):
       return search_min_bst(self.root)

    def search(self, key):
       return search_bst(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, msg='BSTMap :', order=1):
        print(msg, end='')
        if order == 1:
            self.inorder(self.root)
        elif order == 2:
            self.preorder(self.root)
        elif order == 3:
            self.postorder(self.root)
        print()

    def inorder(self, n):
        if n is not None:
            self.inorder(n.left)
            print(n.key, end=' ')
            self.inorder(n.right)

    def preorder(self, n):
        if n is not None:
            print(n.key, end=' ')
            self.preorder(n.left)
            self.preorder(n.right)

    def postorder(self, n):
        if n is not None:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.key, end=' ')

            